import 'package:flutter/material.dart';
import 'package:frontend/screens/auth/home_page.dart';
import 'package:frontend/screens/auth/login_page.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'package:global_configuration/global_configuration.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await GlobalConfiguration().loadFromAsset("app_settings");
  await Supabase.initialize(
    url: GlobalConfiguration().get('SUPABASE_URL'),
    anonKey: GlobalConfiguration().get('SUPABASE_ANON_KEY'),
  );
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(body: LoginPage()),
    );
  }
}
