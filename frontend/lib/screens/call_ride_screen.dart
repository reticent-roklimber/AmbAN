import 'package:amban/providers/app_state_provider.dart';
import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:maplibre_gl/maplibre_gl.dart';

class CallRideScreen extends StatefulWidget {
  @override
  DraggableFABState createState() => DraggableFABState();
}

class DraggableFABState extends State<CallRideScreen> {
  AppStateProvider? _appStateProvider;
  bool _ifEmergency = false;
  bool isFABVisible = true; // Tracks FAB visibility
  Offset fabPosition = Offset(100, 100); // Initial position of the FAB

  void toggleFABVisibility() {
    setState(() {
      isFABVisible = !isFABVisible; // Toggle FAB visibility
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        actions: [
          IconButton(
              onPressed: () => Navigator.pushNamed(context, '/settings'),
              icon: const Icon(Icons.settings))
        ],
      ),
      body: Stack(
        children: <Widget>[
          // Your main content here
          Column(children: [
            // TODO(reticent-roklimber): Change solid colors to gradients
            Expanded(
                child: Container(
              color: Colors.green.shade300,
            )),
            Expanded(child: Container(color: Colors.red.shade300))
          ]),
          Column(mainAxisAlignment: MainAxisAlignment.spaceEvenly, children: [
            Align(
                alignment: Alignment.topCenter,
                child:
                    DragTarget(builder: (context, candidateData, rejectedData) {
                  return Container(
                    width: 96,
                    height: 96,
                    decoration: BoxDecoration(
                        shape: BoxShape.circle, color: Colors.green.shade800),
                  );
                }, onWillAcceptWithDetails: (data) {
                  return true;
                }, onAcceptWithDetails: (data) {
                  _appStateProvider?.checkIfEmergencyCase(false);
                  Navigator.pushReplacementNamed(context, '/home');
                })),
            Align(
              alignment: Alignment.center,
              // left: fabPosition.dx,
              // top: fabPosition.dy,
              child: Draggable(
                data: true,
                axis: Axis.vertical,
                feedback: FloatingActionButton.large(
                  onPressed: () {},
                  child: const Icon(Icons.local_hospital_rounded),
                ),
                childWhenDragging: Container(width: 96, height: 96),
                child: isFABVisible
                    ? FloatingActionButton.large(
                        onPressed: toggleFABVisibility,
                        child: const Icon(Icons.local_hospital_rounded),
                      )
                    : Container(), // Hide FAB when isFABVisible is false
                onDragEnd: (details) {
                  setState(() {
                    fabPosition =
                        details.offset; // Update FAB position when dragged
                  });
                },
              ),
            ),
            Align(
                alignment: Alignment.bottomCenter,
                child:
                    DragTarget(builder: (context, candidateData, rejectedData) {
                  return Container(
                    width: 96,
                    height: 96,
                    decoration: BoxDecoration(
                        shape: BoxShape.circle, color: Colors.red.shade800),
                  );
                }, onWillAcceptWithDetails: (data) {
                  return true;
                }, onAcceptWithDetails: (data) {
                  _appStateProvider?.checkIfEmergencyCase(true);
                  Navigator.pushReplacementNamed(context, '/home');
                })),
          ])
        ],
      ),
    );
  }
}
