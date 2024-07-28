import 'package:flutter/material.dart';
import 'package:frontend/screens/auth/home_page.dart';
import 'package:frontend/screens/auth/register_page.dart';
import 'package:frontend/utils/constants.dart';
import 'package:frontend/utils/snackbar_extension.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  bool _isLoading = false;
  GlobalKey<FormState> _formKey = GlobalKey();
  late TextEditingController _emailController;
  late TextEditingController _passwordController;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    _emailController = TextEditingController();
    _passwordController = TextEditingController();
  }

  @override
  void dispose() {
    // TODO: implement dispose
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  void _signIn() async {
    final _isValid = _formKey.currentState?.validate();
    if (_isValid != null && _isValid) {
      setState(() {
        _isLoading = true;
      });
      try {
        await supabase.auth.signInWithPassword(
            email: _emailController.text, password: _passwordController.text);

        setState(() {
          _isLoading = false;
        });
        _navigateToHome();
      } on AuthException catch (e) {
        context.showSnackbar(message: e.message, backgroundColor: Colors.red);
        setState(() {
          _isLoading = false;
        });
      } catch (e) {
        context.showSnackbar(
            message: e.toString(), backgroundColor: Colors.red);
      }
    }
  }

  void _navigateToHome() {
    Navigator.of(context).push(
        //LoginPage.route()
        MaterialPageRoute(builder: (_) => const HomePage()));
    // Navigator.pushNamedAndRemoveUntil(
    //   context,
    //   MaterialPageRoute(builder: (_) => const HomePage()) as String,
    //   (route) => false,
    // );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Login'),
        centerTitle: true,
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Form(
            key: _formKey,
            child: Column(
              children: [
                if (_isLoading) ...[
                  const Center(
                    child: CircularProgressIndicator.adaptive(),
                  )
                ],
                const SizedBox(height: 16.0),
                TextFormField(
                  keyboardType: TextInputType.emailAddress,
                  textInputAction: TextInputAction.next,
                  maxLines: 1,
                  autofocus: false,
                  controller: _emailController,
                  decoration: InputDecoration(
                    hintText: "Enter your email",
                    labelText: 'Email',
                    //floatingLabelBehavior:
                    border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(8.0),
                        borderSide: BorderSide(
                            color: Theme.of(context).primaryColorDark,
                            width: 1)),
                    focusedBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(8.0),
                      borderSide: BorderSide(
                        color: Theme.of(context).primaryColor,
                        width: 1,
                      ),
                    ),
                    contentPadding: const EdgeInsets.all(8),
                  ),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'email is empty';
                    }
                    return null;
                  },
                ),
                TextFormField(
                  keyboardType: TextInputType.visiblePassword,
                  textInputAction: TextInputAction.next,
                  //obscureText: true,
                  maxLines: 1,
                  autofocus: false,
                  controller: _passwordController,
                  decoration: InputDecoration(
                    hintText: "Enter your password",
                    labelText: 'password',
                    //floatingLabelBehavior:
                    border: OutlineInputBorder(
                        borderRadius: BorderRadius.circular(8.0),
                        borderSide: BorderSide(
                            color: Theme.of(context).primaryColorDark,
                            width: 1)),
                    focusedBorder: OutlineInputBorder(
                      borderRadius: BorderRadius.circular(8.0),
                      borderSide: BorderSide(
                        color: Theme.of(context).primaryColor,
                        width: 1,
                      ),
                    ),
                    contentPadding: const EdgeInsets.all(8),
                  ),
                  validator: (value) {
                    if (value == null || value.isEmpty) {
                      return 'email is empty';
                    }
                    if (value.length < 6) {
                      return 'password length must be 6 char or more';
                    }
                    return null;
                  },
                ),
                const SizedBox(
                  height: 16.0,
                ),
                FilledButton(
                  onPressed: _isLoading ? null : _signIn,
                  child: const Text('Login'),
                ),
                const SizedBox(height: 8.0),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    const Text("'Don't have an account ?"),
                    TextButton(
                      onPressed: () {
                        Navigator.of(context).push(MaterialPageRoute(
                            builder: (_) => const RegisterPage()));
                      },
                      child: const Text('Register'),
                    )
                  ],
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
