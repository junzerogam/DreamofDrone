#ifndef QOS_ESTIMATOR_H
#define QOS_ESTIMATOR_H

#include <gst/gst.h>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <gst/rtp/gstrtcpbuffer.h>
#include <sys/time.h>

#include "NTPTime.h"
#include "DeviceDatatypes.h"

// Computes Quality-of-Service of the network per RTT of RTCP packets by maintaining
// timers and state information about bytes transferred. The information recorded
// per RTT is saved in a QoSReport struct which can be accessed by other classes

class QoSEstimator
{
private:
    gfloat smooth_rtt;
    guint64 prev_rr_time;
    guint32 prev_pkt_count;
    gfloat prev_buffer_occ;
    gfloat rtp_size;
    guint32 bytes_transferred;
    gfloat smooth_enc_bitrate;
    guint64 last_bytes_sent;
    guint64 rtph_bytes_interval;

    timeval prev_tv;
    timeval prev_bw_tv;

    gfloat estimated_bitrate;
    gfloat encoding_bitrate;

    guint64 get_current_ntp_time();
    guint32 get_compressed_ntp_time(const guint64 &full_ntp_timestamp);

    QoSReport qos_report;

    void process_rr_packet(GstRTCPPacket* packet);
    void process_sr_packet(GstRTCPPacket* packet);
    gfloat update_rtt(const guint32 &lsr, const guint32 &dlsr);
    static void exp_smooth_val(const gfloat &curr_val, gfloat &smooth_val, gfloat alpha);

public:
    QoSEstimator();
    ~QoSEstimator();
    QoSReport get_qos_report();
    void calculate_bitrates(const guint64 &bytes_sent, const guint32 &buffer_size);
    void handle_rtcp_packet(GstRTCPPacket* packet);
};

#endif