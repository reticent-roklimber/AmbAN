import 'package:amban/providers/app_state_provider.dart';
import 'package:flutter/material.dart';
import 'package:global_configuration/global_configuration.dart';
import 'package:provider/provider.dart';
// import 'package:supabase_auth_ui/supabase_auth_ui.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

import 'package:amban/routes/app_routes.dart';

var globalMessengerKey = GlobalKey<ScaffoldMessengerState>();

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  // await GlobalConfiguration().loadFromAsset("app_settings");
  // await Supabase.initialize(
  //   url: GlobalConfiguration().get('SUPABASE_URL'),
  //   anonKey: GlobalConfiguration().get('SUPABASE_ANON_KEY'),
  // );

  runApp(
    MultiProvider(providers: [
      ChangeNotifierProvider<AppStateProvider>(
          create: (_) => AppStateProvider())
    ], child: AmbanApp()),
  );
}

// final supabase = Supabase.instance.client;

class AmbanApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'AmbAN ',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      routes: AppRoutes.routes(),
      // initialRoute: Provider.of<SignInProvider>(context).isLoggedIn
      //     ? '/home'
      //     : '/authentication'
      initialRoute: '/call-ride',
      scaffoldMessengerKey: globalMessengerKey,
    );
  }
}
