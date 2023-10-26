from django.test import TestCase, Client
from django.http import HttpResponseRedirect


class TestCommentView(TestCase):
    def test_post_comment_when_content_length_less_than_10_then_return_validation_error(self):
        client = Client()
        form_data = {
            'nickname': 'jack',
            'email': 'foo@bar.com',
            'website': 'https://baidu.com',
            'content': 'zz',
            'target': 'https://target.com'
        }

        response = client.post('/comment/', form_data)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'comment/result.html')

        context = response.context
        self.assertEquals(context['succeed'], False)
        self.assertEquals(context['form'].errors['content'][0], '内容长度怎么能这么短呢！！！')
        self.assertEquals(context['target'], 'https://target.com')

    def test_post_comment_when_valid_then_redirect_to_target(self):
        client = Client()
        form_data = {
            'nickname': 'jack',
            'email': 'foo@bar.com',
            'website': 'https://baidu.com',
            'content': 'zzzzzzzzzzzzz',
            'target': 'https://target.com'
        }

        response = client.post('/comment/', form_data)

        self.assertIsInstance(response, HttpResponseRedirect)
        self.assertEqual(response.url, 'https://target.com')
