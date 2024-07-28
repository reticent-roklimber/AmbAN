import 'package:flutter/material.dart';
import 'package:amban/screens/call_ride_screen.dart';
import 'package:amban/screens/settings_screen.dart';

// import 'package:frontend/screens/auth_screen.dart';
import 'package:amban/screens/homepage_screen.dart';
import 'package:amban/screens/profile_screen.dart';

class AppRoutes {
  static Map<String, WidgetBuilder> routes() => {
        // '/authentication': (BuildContext context) => AuthenticationWidget(),
        // '/otp_overlay': (BuildContext context) => OtpInputWidget(),
        '/call-ride': (BuildContext context) => CallRideScreen(),
        '/home': (BuildContext context) => HomePageScreen(),
        '/profile': (BuildContext context) => ProfileScreen(),
        '/settings': (BuildContext context) => SettingScreen(),
      };
}
