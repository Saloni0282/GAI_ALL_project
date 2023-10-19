import unittest
from flask import Flask ,url_for
from app import create_app ,db
class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app=create_app("testing")
        self.app_context=self.app.app_context()
        self


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_postt(self):
        response = self.clientpost(url_for("create_post",data{
            "title":"me",
            "content":"nothing to do"
        }))
        self.assertEqual(response.status_code,200)
        self.assertIn(response.data)