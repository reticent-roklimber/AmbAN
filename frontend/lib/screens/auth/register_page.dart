import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:frontend/screens/auth/home_page.dart';
import 'package:frontend/screens/auth/login_page.dart';
import 'package:frontend/utils/constants.dart';
import 'package:frontend/utils/snackbar_extension.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({super.key});

  @override
  State<RegisterPage> createState() => RegisterPageState();
}

class RegisterPageState extends State<RegisterPage> {
  bool _isLoading = false;
  GlobalKey<FormState> _formKey = GlobalKey();
  late TextEditingController _emailController;
  late TextEditingController _passwordController;
  late TextEditingController _nameController;

  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    _nameController = TextEditingController();
    _emailController = TextEditingController();
    _passwordController = TextEditingController();
  }

  @override
  void dispose() {
    // TODO: implement dispose
    _emailController.dispose();
    _passwordController.dispose();
    _nameController.dispose();
    super.dispose();
  }

  void _signUp() async {
    final isValid = _formKey.currentState?.validate();
    if (isValid != null && isValid) {
      try {
        setState(() {
          _isLoading = true;
        });

        // final isEmailExist = await supabase
        //     .from('profiles')
        //     .select('email')
        //     .eq('email', _emailController.text)
        //     .limit(1)
        //     .maybeSingle();
        // if (isEmailExist != null &&
        //     isEmailExist['email'].toString().isNotEmpty) {
        //   throw const AuthException('email already exists');
        // }
        await supabase.auth.signUp(
            email: _emailController.text,
            password: _passwordController.text,
            data: {'name': _nameController.text.toLowerCase()});

        setState(() {
          _isLoading = false;
        });

        _navigateToLoginPage();
      } on AuthException catch (e) {
        context.showSnackbar(message: e.message, backgroundColor: Colors.red);
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  void _navigateToLoginPage() {
    Navigator.of(context).push(
        //LoginPage.route()
        MaterialPageRoute(builder: (_) => const HomePage()));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text('Register'),
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
                          keyboardType: TextInputType.text,
                          textInputAction: TextInputAction.next,
                          maxLines: 1,
                          autofocus: false,
                          controller: _nameController,
                          decoration: InputDecoration(
                            hintText: "Enter your name",
                            labelText: 'Name',
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
                              return 'name is empty';
                            }
                            return null;
                          },
                        ),
                        TextFormField(
                          keyboardType: TextInputType.emailAddress,
                          textInputAction: TextInputAction.next,
                          maxLines: 2,
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
                        const SizedBox(height: 24.0),
                        FilledButton(
                          onPressed: _isLoading ? null : _signUp,
                          child: const Text('Register'),
                        ),
                        TextButton(
                          onPressed: () {
                            _navigateToLoginPage();
                          },
                          child: const Text("I already have an account"),
                        )
                      ],
                    )))));
  }
}
