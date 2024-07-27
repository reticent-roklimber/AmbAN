import 'package:flutter/material.dart';

import 'package:frontend/screens/auth_screen.dart';
import 'package:frontend/screens/homepage_screen.dart';
import 'package:frontend/screens/profile_screen.dart';

class AppRoutes {
  static Map<String, WidgetBuilder> routes() => {
        // '/authentication': (BuildContext context) => AuthenticationWidget(),
        // '/otp_overlay': (BuildContext context) => OtpInputWidget(),
        '/home': (BuildContext context) => HomePageWidget(),
        // '/profile': (BuildContext context) => ProfileWidget(),
      };
}
