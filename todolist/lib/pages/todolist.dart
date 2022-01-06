import 'package:flutter/material.dart';
import 'package:todolist/pages/add.dart';

import 'package:http/http.dart' as http;
import 'dart:async';
import 'dart:convert';

import 'package:todolist/pages/update_todolist.dart';

class Todolist extends StatefulWidget {
  const Todolist({Key? key}) : super(key: key);

  @override
  _TodolistState createState() => _TodolistState();
}

class _TodolistState extends State<Todolist> {
  List todolistitems = [];

  @override
  void initState() {
    // TODO: implement initState
    super.initState();
    getTodolist();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.push(
                  context, MaterialPageRoute(builder: (context) => AddPage()))
              .then((value) {
            setState(() {
              print(value);

              getTodolist();
            });
          });
        },
        child: Icon(Icons.add),
      ),
      appBar: AppBar(
        actions: [
          IconButton(
              onPressed: () {
                setState(() {
                  getTodolist(); // รีเฟรสหน้าใหม่
                });
              },
              icon: Icon(
                Icons.refresh,
                color: Colors.deepOrangeAccent,
              ))
        ],
        title: Text('All Todolist'),
      ),
      body: todolistCreate(),
    );
  }

  Widget todolistCreate() {
    return ListView.builder(
        itemCount: todolistitems.length,
        itemBuilder: (context, index) {
          return Card(
            child: ListTile(
              title: Text('${todolistitems[index]['title']}'),
              onTap: () {
                Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => UpdatePage(
                            todolistitems[index]['id'],
                            todolistitems[index]['title'],
                            todolistitems[index]['detail']))).then((value) {
                  setState(() {
                    getTodolist();
                  });
                });
              },
            ),
          );
        });
  }

  Future<void> getTodolist() async {
    List alltodo = [];
    var url = Uri.http('192.168.10.67:8000', '/api/all-todolist');
    var response = await http.get(url);
    var result = utf8.decode(response.bodyBytes);
    //print(result);
    setState(() {
      todolistitems = jsonDecode(result);
    });
  }
}
