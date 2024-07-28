import 'package:flutterflow_ui/flutterflow_ui.dart';
// import 'package:gather/components/data_text_form_widget.dart';
import 'package:flutter/material.dart';
import 'package:flutter_map/flutter_map.dart';
import 'package:latlong2/latlong.dart' as latlong;
// import 'package:frontend/components/map_widget.dart';
// import 'package:font_awesome_flutter/font_awesome_flutter.dart';
// import 'package:gather/components/floating_camera_widget.dart';
// import 'package:gather/models/list_view_model.dart';
// import 'package:gather/components/appbar_widget.dart';
// import 'package:gather/components/drawer_widget.dart';

class HomePageScreen extends StatefulWidget {
  const HomePageScreen({super.key});

  @override
  State<HomePageScreen> createState() => _HomePageScreenState();
}

class _HomePageScreenState extends State<HomePageScreen> {
  // late HomePageScreen _model;

  final scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void initState() {
    super.initState();
  }

  @override
  void dispose() {
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () => {},
      child: Scaffold(
        appBar: AppBar(),
        body: Stack(children: [
          FlutterMap(
              options: MapOptions(
                center: latlong.LatLng(51.509364, -0.128928),
                zoom: 3.2,
              ),
              children: [
                TileLayer(
                  urlTemplate: 'https://tile.openstreetmap.org/{z}/{x}/{y}.png',
                  userAgentPackageName: 'com.amban.app',
                ),
              ])
        ]),
      ),
    );
  }
}
