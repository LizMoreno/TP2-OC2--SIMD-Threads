#! /usr/bin/env python3

# Programs that are runnable.
ns3_runnable_programs = ['build/src/aodv/examples/ns3.31-aodv-optimized', 'build/src/applications/examples/ns3.31-three-gpp-http-example-optimized', 'build/src/bridge/examples/ns3.31-csma-bridge-optimized', 'build/src/bridge/examples/ns3.31-csma-bridge-one-hop-optimized', 'build/src/buildings/examples/ns3.31-buildings-pathloss-profiler-optimized', 'build/src/buildings/examples/ns3.31-outdoor-random-walk-example-optimized', 'build/src/config-store/examples/ns3.31-config-store-save-optimized', 'build/src/core/examples/ns3.31-main-callback-optimized', 'build/src/core/examples/ns3.31-sample-simulator-optimized', 'build/src/core/examples/ns3.31-main-ptr-optimized', 'build/src/core/examples/ns3.31-main-random-variable-stream-optimized', 'build/src/core/examples/ns3.31-sample-random-variable-optimized', 'build/src/core/examples/ns3.31-sample-random-variable-stream-optimized', 'build/src/core/examples/ns3.31-command-line-example-optimized', 'build/src/core/examples/ns3.31-hash-example-optimized', 'build/src/core/examples/ns3.31-sample-log-time-format-optimized', 'build/src/core/examples/ns3.31-test-string-value-formatting-optimized', 'build/src/core/examples/ns3.31-sample-show-progress-optimized', 'build/src/core/examples/ns3.31-empirical-random-variable-example-optimized', 'build/src/core/examples/ns3.31-system-path-examples-optimized', 'build/src/core/examples/ns3.31-main-test-sync-optimized', 'build/src/csma/examples/ns3.31-csma-one-subnet-optimized', 'build/src/csma/examples/ns3.31-csma-broadcast-optimized', 'build/src/csma/examples/ns3.31-csma-packet-socket-optimized', 'build/src/csma/examples/ns3.31-csma-multicast-optimized', 'build/src/csma/examples/ns3.31-csma-raw-ip-socket-optimized', 'build/src/csma/examples/ns3.31-csma-ping-optimized', 'build/src/csma-layout/examples/ns3.31-csma-star-optimized', 'build/src/dsdv/examples/ns3.31-dsdv-manet-optimized', 'build/src/dsr/examples/ns3.31-dsr-optimized', 'build/src/energy/examples/ns3.31-li-ion-energy-source-optimized', 'build/src/energy/examples/ns3.31-rv-battery-model-test-optimized', 'build/src/energy/examples/ns3.31-basic-energy-model-test-optimized', 'build/src/fd-net-device/examples/ns3.31-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3.31-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3.31-realtime-dummy-network-optimized', 'build/src/fd-net-device/examples/ns3.31-realtime-fd2fd-onoff-optimized', 'build/src/fd-net-device/examples/ns3.31-fd-emu-ping-optimized', 'build/src/fd-net-device/examples/ns3.31-fd-emu-udp-echo-optimized', 'build/src/fd-net-device/examples/ns3.31-fd-emu-onoff-optimized', 'build/src/fd-net-device/examples/ns3.31-fd-tap-ping-optimized', 'build/src/fd-net-device/examples/ns3.31-fd-tap-ping6-optimized', 'build/src/internet/examples/ns3.31-main-simple-optimized', 'build/src/internet-apps/examples/ns3.31-dhcp-example-optimized', 'build/src/internet-apps/examples/ns3.31-traceroute-example-optimized', 'build/src/lr-wpan/examples/ns3.31-lr-wpan-packet-print-optimized', 'build/src/lr-wpan/examples/ns3.31-lr-wpan-phy-test-optimized', 'build/src/lr-wpan/examples/ns3.31-lr-wpan-data-optimized', 'build/src/lr-wpan/examples/ns3.31-lr-wpan-error-model-plot-optimized', 'build/src/lr-wpan/examples/ns3.31-lr-wpan-error-distance-plot-optimized', 'build/src/lr-wpan/examples/ns3.31-lr-wpan-mlme-optimized', 'build/src/lte/examples/ns3.31-lena-cqi-threshold-optimized', 'build/src/lte/examples/ns3.31-lena-dual-stripe-optimized', 'build/src/lte/examples/ns3.31-lena-fading-optimized', 'build/src/lte/examples/ns3.31-lena-intercell-interference-optimized', 'build/src/lte/examples/ns3.31-lena-ipv6-addr-conf-optimized', 'build/src/lte/examples/ns3.31-lena-ipv6-ue-rh-optimized', 'build/src/lte/examples/ns3.31-lena-ipv6-ue-ue-optimized', 'build/src/lte/examples/ns3.31-lena-pathloss-traces-optimized', 'build/src/lte/examples/ns3.31-lena-profiling-optimized', 'build/src/lte/examples/ns3.31-lena-rem-optimized', 'build/src/lte/examples/ns3.31-lena-rem-sector-antenna-optimized', 'build/src/lte/examples/ns3.31-lena-rlc-traces-optimized', 'build/src/lte/examples/ns3.31-lena-simple-optimized', 'build/src/lte/examples/ns3.31-lena-simple-epc-optimized', 'build/src/lte/examples/ns3.31-lena-simple-epc-backhaul-optimized', 'build/src/lte/examples/ns3.31-lena-deactivate-bearer-optimized', 'build/src/lte/examples/ns3.31-lena-x2-handover-optimized', 'build/src/lte/examples/ns3.31-lena-x2-handover-measures-optimized', 'build/src/lte/examples/ns3.31-lena-frequency-reuse-optimized', 'build/src/lte/examples/ns3.31-lena-distributed-ffr-optimized', 'build/src/lte/examples/ns3.31-lena-uplink-power-control-optimized', 'build/src/lte/examples/ns3.31-lena-radio-link-failure-optimized', 'build/src/lte/examples/ns3.31-lena-simple-epc-emu-optimized', 'build/src/mesh/examples/ns3.31-mesh-optimized', 'build/src/mobility/examples/ns3.31-main-grid-topology-optimized', 'build/src/mobility/examples/ns3.31-main-random-topology-optimized', 'build/src/mobility/examples/ns3.31-main-random-walk-optimized', 'build/src/mobility/examples/ns3.31-mobility-trace-example-optimized', 'build/src/mobility/examples/ns3.31-ns2-mobility-trace-optimized', 'build/src/mobility/examples/ns3.31-bonnmotion-ns2-example-optimized', 'build/src/netanim/examples/ns3.31-dumbbell-animation-optimized', 'build/src/netanim/examples/ns3.31-grid-animation-optimized', 'build/src/netanim/examples/ns3.31-star-animation-optimized', 'build/src/netanim/examples/ns3.31-wireless-animation-optimized', 'build/src/netanim/examples/ns3.31-uan-animation-optimized', 'build/src/netanim/examples/ns3.31-colors-link-description-optimized', 'build/src/netanim/examples/ns3.31-resources-counters-optimized', 'build/src/network/examples/ns3.31-main-packet-header-optimized', 'build/src/network/examples/ns3.31-main-packet-tag-optimized', 'build/src/network/examples/ns3.31-packet-socket-apps-optimized', 'build/src/nix-vector-routing/examples/ns3.31-nix-simple-optimized', 'build/src/nix-vector-routing/examples/ns3.31-nms-p2p-nix-optimized', 'build/src/olsr/examples/ns3.31-simple-point-to-point-olsr-optimized', 'build/src/olsr/examples/ns3.31-olsr-hna-optimized', 'build/src/point-to-point/examples/ns3.31-main-attribute-value-optimized', 'build/src/propagation/examples/ns3.31-main-propagation-loss-optimized', 'build/src/propagation/examples/ns3.31-jakes-propagation-model-example-optimized', 'build/src/sixlowpan/examples/ns3.31-example-sixlowpan-optimized', 'build/src/sixlowpan/examples/ns3.31-example-ping-lr-wpan-optimized', 'build/src/sixlowpan/examples/ns3.31-example-ping-lr-wpan-beacon-optimized', 'build/src/sixlowpan/examples/ns3.31-example-ping-lr-wpan-mesh-under-optimized', 'build/src/spectrum/examples/ns3.31-adhoc-aloha-ideal-phy-optimized', 'build/src/spectrum/examples/ns3.31-adhoc-aloha-ideal-phy-matrix-propagation-loss-model-optimized', 'build/src/spectrum/examples/ns3.31-adhoc-aloha-ideal-phy-with-microwave-oven-optimized', 'build/src/spectrum/examples/ns3.31-tv-trans-example-optimized', 'build/src/spectrum/examples/ns3.31-tv-trans-regional-example-optimized', 'build/src/spectrum/examples/ns3.31-three-gpp-channel-example-optimized', 'build/src/stats/examples/ns3.31-gnuplot-example-optimized', 'build/src/stats/examples/ns3.31-double-probe-example-optimized', 'build/src/stats/examples/ns3.31-time-probe-example-optimized', 'build/src/stats/examples/ns3.31-gnuplot-aggregator-example-optimized', 'build/src/stats/examples/ns3.31-gnuplot-helper-example-optimized', 'build/src/stats/examples/ns3.31-file-aggregator-example-optimized', 'build/src/stats/examples/ns3.31-file-helper-example-optimized', 'build/src/tap-bridge/examples/ns3.31-tap-csma-optimized', 'build/src/tap-bridge/examples/ns3.31-tap-csma-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3.31-tap-wifi-virtual-machine-optimized', 'build/src/tap-bridge/examples/ns3.31-tap-wifi-dumbbell-optimized', 'build/src/topology-read/examples/ns3.31-topology-example-sim-optimized', 'build/src/traffic-control/examples/ns3.31-red-tests-optimized', 'build/src/traffic-control/examples/ns3.31-red-vs-ared-optimized', 'build/src/traffic-control/examples/ns3.31-adaptive-red-tests-optimized', 'build/src/traffic-control/examples/ns3.31-pfifo-vs-red-optimized', 'build/src/traffic-control/examples/ns3.31-codel-vs-pfifo-basic-test-optimized', 'build/src/traffic-control/examples/ns3.31-codel-vs-pfifo-asymmetric-optimized', 'build/src/traffic-control/examples/ns3.31-pie-example-optimized', 'build/src/uan/examples/ns3.31-uan-cw-example-optimized', 'build/src/uan/examples/ns3.31-uan-rc-example-optimized', 'build/src/uan/examples/ns3.31-uan-raw-example-optimized', 'build/src/uan/examples/ns3.31-uan-ipv4-example-optimized', 'build/src/uan/examples/ns3.31-uan-ipv6-example-optimized', 'build/src/uan/examples/ns3.31-uan-6lowpan-example-optimized', 'build/src/virtual-net-device/examples/ns3.31-virtual-net-device-optimized', 'build/src/wave/examples/ns3.31-wave-simple-80211p-optimized', 'build/src/wave/examples/ns3.31-wave-simple-device-optimized', 'build/src/wave/examples/ns3.31-vanet-routing-compare-optimized', 'build/src/wifi/examples/ns3.31-wifi-phy-test-optimized', 'build/src/wifi/examples/ns3.31-wifi-test-interference-helper-optimized', 'build/src/wifi/examples/ns3.31-wifi-manager-example-optimized', 'build/src/wifi/examples/ns3.31-wifi-trans-example-optimized', 'build/src/wifi/examples/ns3.31-wifi-phy-configuration-optimized', 'build/src/wifi/examples/ns3.31-wifi-bianchi-optimized', 'build/src/wimax/examples/ns3.31-wimax-ipv4-optimized', 'build/src/wimax/examples/ns3.31-wimax-multicast-optimized', 'build/src/wimax/examples/ns3.31-wimax-simple-optimized', 'build/examples/stats/ns3.31-wifi-example-sim-optimized', 'build/examples/error-model/ns3.31-simple-error-model-optimized', 'build/examples/routing/ns3.31-dynamic-global-routing-optimized', 'build/examples/routing/ns3.31-static-routing-slash32-optimized', 'build/examples/routing/ns3.31-global-routing-slash32-optimized', 'build/examples/routing/ns3.31-global-injection-slash32-optimized', 'build/examples/routing/ns3.31-simple-global-routing-optimized', 'build/examples/routing/ns3.31-simple-alternate-routing-optimized', 'build/examples/routing/ns3.31-mixed-global-routing-optimized', 'build/examples/routing/ns3.31-simple-routing-ping6-optimized', 'build/examples/routing/ns3.31-manet-routing-compare-optimized', 'build/examples/routing/ns3.31-ripng-simple-network-optimized', 'build/examples/routing/ns3.31-rip-simple-network-optimized', 'build/examples/routing/ns3.31-global-routing-multi-switch-plus-router-optimized', 'build/examples/routing/ns3.31-simple-multicast-flooding-optimized', 'build/examples/tcp/ns3.31-tcp-large-transfer-optimized', 'build/examples/tcp/ns3.31-tcp-nsc-lfn-optimized', 'build/examples/tcp/ns3.31-tcp-nsc-zoo-optimized', 'build/examples/tcp/ns3.31-tcp-star-server-optimized', 'build/examples/tcp/ns3.31-star-optimized', 'build/examples/tcp/ns3.31-tcp-bulk-send-optimized', 'build/examples/tcp/ns3.31-tcp-pcap-nanosec-example-optimized', 'build/examples/tcp/ns3.31-tcp-nsc-comparison-optimized', 'build/examples/tcp/ns3.31-tcp-variants-comparison-optimized', 'build/examples/tcp/ns3.31-tcp-pacing-optimized', 'build/examples/tcp/ns3.31-dctcp-example-optimized', 'build/examples/naming/ns3.31-object-names-optimized', 'build/examples/energy/ns3.31-energy-model-example-optimized', 'build/examples/energy/ns3.31-energy-model-with-harvesting-example-optimized', 'build/examples/traffic-control/ns3.31-traffic-control-optimized', 'build/examples/traffic-control/ns3.31-queue-discs-benchmark-optimized', 'build/examples/traffic-control/ns3.31-red-vs-fengadaptive-optimized', 'build/examples/traffic-control/ns3.31-red-vs-nlred-optimized', 'build/examples/traffic-control/ns3.31-tbf-example-optimized', 'build/examples/traffic-control/ns3.31-cobalt-vs-codel-optimized', 'build/examples/udp-client-server/ns3.31-udp-client-server-optimized', 'build/examples/udp-client-server/ns3.31-udp-trace-client-server-optimized', 'build/examples/wireless/ns3.31-mixed-wired-wireless-optimized', 'build/examples/wireless/ns3.31-wifi-adhoc-optimized', 'build/examples/wireless/ns3.31-wifi-clear-channel-cmu-optimized', 'build/examples/wireless/ns3.31-wifi-ap-optimized', 'build/examples/wireless/ns3.31-wifi-wired-bridging-optimized', 'build/examples/wireless/ns3.31-wifi-multirate-optimized', 'build/examples/wireless/ns3.31-wifi-simple-adhoc-optimized', 'build/examples/wireless/ns3.31-wifi-simple-adhoc-grid-optimized', 'build/examples/wireless/ns3.31-wifi-simple-infra-optimized', 'build/examples/wireless/ns3.31-wifi-simple-interference-optimized', 'build/examples/wireless/ns3.31-wifi-blockack-optimized', 'build/examples/wireless/ns3.31-wifi-dsss-validation-optimized', 'build/examples/wireless/ns3.31-wifi-ofdm-validation-optimized', 'build/examples/wireless/ns3.31-wifi-ofdm-ht-validation-optimized', 'build/examples/wireless/ns3.31-wifi-ofdm-vht-validation-optimized', 'build/examples/wireless/ns3.31-wifi-hidden-terminal-optimized', 'build/examples/wireless/ns3.31-wifi-ht-network-optimized', 'build/examples/wireless/ns3.31-wifi-vht-network-optimized', 'build/examples/wireless/ns3.31-wifi-timing-attributes-optimized', 'build/examples/wireless/ns3.31-wifi-sleep-optimized', 'build/examples/wireless/ns3.31-wifi-power-adaptation-distance-optimized', 'build/examples/wireless/ns3.31-wifi-power-adaptation-interference-optimized', 'build/examples/wireless/ns3.31-wifi-rate-adaptation-distance-optimized', 'build/examples/wireless/ns3.31-wifi-aggregation-optimized', 'build/examples/wireless/ns3.31-wifi-txop-aggregation-optimized', 'build/examples/wireless/ns3.31-wifi-simple-ht-hidden-stations-optimized', 'build/examples/wireless/ns3.31-wifi-80211n-mimo-optimized', 'build/examples/wireless/ns3.31-wifi-mixed-network-optimized', 'build/examples/wireless/ns3.31-wifi-tcp-optimized', 'build/examples/wireless/ns3.31-wifi-80211e-txop-optimized', 'build/examples/wireless/ns3.31-wifi-spectrum-per-example-optimized', 'build/examples/wireless/ns3.31-wifi-spectrum-per-interference-optimized', 'build/examples/wireless/ns3.31-wifi-spectrum-saturation-example-optimized', 'build/examples/wireless/ns3.31-wifi-ofdm-he-validation-optimized', 'build/examples/wireless/ns3.31-wifi-he-network-optimized', 'build/examples/wireless/ns3.31-wifi-multi-tos-optimized', 'build/examples/wireless/ns3.31-wifi-backward-compatibility-optimized', 'build/examples/wireless/ns3.31-wifi-pcf-optimized', 'build/examples/wireless/ns3.31-wifi-spatial-reuse-optimized', 'build/examples/socket/ns3.31-socket-bound-static-routing-optimized', 'build/examples/socket/ns3.31-socket-bound-tcp-static-routing-optimized', 'build/examples/socket/ns3.31-socket-options-ipv4-optimized', 'build/examples/socket/ns3.31-socket-options-ipv6-optimized', 'build/examples/realtime/ns3.31-realtime-udp-echo-optimized', 'build/examples/tutorial/ns3.31-hello-simulator-optimized', 'build/examples/tutorial/ns3.31-first-optimized', 'build/examples/tutorial/ns3.31-second-optimized', 'build/examples/tutorial/ns3.31-third-optimized', 'build/examples/tutorial/ns3.31-fourth-optimized', 'build/examples/tutorial/ns3.31-fifth-optimized', 'build/examples/tutorial/ns3.31-sixth-optimized', 'build/examples/tutorial/ns3.31-seventh-optimized', 'build/examples/ipv6/ns3.31-icmpv6-redirect-optimized', 'build/examples/ipv6/ns3.31-ping6-optimized', 'build/examples/ipv6/ns3.31-radvd-optimized', 'build/examples/ipv6/ns3.31-radvd-two-prefix-optimized', 'build/examples/ipv6/ns3.31-test-ipv6-optimized', 'build/examples/ipv6/ns3.31-fragmentation-ipv6-optimized', 'build/examples/ipv6/ns3.31-fragmentation-ipv6-two-MTU-optimized', 'build/examples/ipv6/ns3.31-loose-routing-ipv6-optimized', 'build/examples/ipv6/ns3.31-wsn-ping6-optimized', 'build/examples/matrix-topology/ns3.31-matrix-topology-optimized', 'build/examples/udp/ns3.31-udp-echo-optimized', 'build/scratch/subdir/ns3.31-subdir-optimized', 'build/scratch/ns3.31-scratch-simulator-optimized']

# Scripts that are runnable.
ns3_runnable_scripts = ['csma-bridge.py', 'sample-simulator.py', 'wifi-olsr-flowmon.py', 'tap-csma-virtual-machine.py', 'tap-wifi-virtual-machine.py', 'simple-routing-ping6.py', 'mixed-wired-wireless.py', 'wifi-ap.py', 'realtime-udp-echo.py', 'first.py', 'second.py', 'third.py']

