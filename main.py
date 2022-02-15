from src.FugroTools import Request


if __name__ == '__main__':
    url_summary = 'https://jsonplaceholder.typicode.com/comments?postId=1'
    jsonData = {
                  "userId": 1,
                  "id": 1,
                  "title": "2",
                  "body": "3"
                }
    ret = Request.GetData(url_summary, jsonData)
    print("Success")

