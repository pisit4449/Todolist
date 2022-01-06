import 'package:flutter/material.dart';

import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

class AddPage extends StatefulWidget {
  const AddPage({Key? key}) : super(key: key);

  @override
  _AddPageState createState() => _AddPageState();
}

class _AddPageState extends State<AddPage> {
  TextEditingController todo_title = TextEditingController();
  TextEditingController todo_detail = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("เพิ่มข้อมูล"),
      ),
      body: Padding(
        padding: const EdgeInsets.all(20),
        child: ListView(
          children: [
            TextField(
                controller: todo_title,
                decoration: InputDecoration(
                    labelText: 'รายการที่ต้องทำ',
                    border: OutlineInputBorder())),
            SizedBox(height: 20),
            TextField(
                minLines: 4,
                maxLines: 8,
                controller: todo_detail,
                decoration: InputDecoration(
                    labelText: 'รายละเอียดข้อมูล',
                    border: OutlineInputBorder())),
            SizedBox(height: 20),
            Padding(
              padding: const EdgeInsets.all(20),
              child: ElevatedButton(
                onPressed: () {
                  // print("-----------------");
                  // print("title : ${todo_title.text}");
                  // print("detail : ${todo_detail.text}");
                  postTodo();
                  todo_title.clear();
                  todo_detail.clear();
                },
                child: Text("เพิ่มรายการ"),
                style: ButtonStyle(
                    backgroundColor:
                        MaterialStateProperty.all(Colors.amber[400]),
                    padding: MaterialStateProperty.all(
                        EdgeInsets.fromLTRB(50, 20, 50, 20)),
                    textStyle:
                        MaterialStateProperty.all(TextStyle(fontSize: 30))),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Future postTodo() async {
    //var url = Uri.https("fc3e-171-100-241-30.ngrok.io", "/api/post-todolist");
    var url = Uri.http("192.168.10.67:8000", "/api/post-todolist");
    Map<String, String> header = {"Content-type": "application/json"};
    String jsondata =
        '{"title":"${todo_title.text}","detail":"${todo_detail.text}"}';
    var response = await http.post(url, headers: header, body: jsondata);
    print('--------------');
    print(response.body);
  }
}
