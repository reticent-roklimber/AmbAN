import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class AppStateProvider with ChangeNotifier {
  bool _ifEmergencyCase = false;

  AppStateProvider();

  bool get ifEmergencyCase => _ifEmergencyCase;

  void checkIfEmergencyCase(ifEmergencyCase) {
    _ifEmergencyCase = ifEmergencyCase;
    notifyListeners();
  }
}
