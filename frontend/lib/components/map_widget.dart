import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart' as latlong;
import 'package:flutterflow_ui/flutterflow_ui.dart';

class flutterMapWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return FlutterMap(
        options: MapOptions(
          center: latlong.LatLng(51.509364, -0.128928),
          zoom: 3.2,
        ),
        children: [
          TileLayer(
            urlTemplate: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
            userAgentPackageName: 'com.amban.app',
          ),
        ]);
  }
}
