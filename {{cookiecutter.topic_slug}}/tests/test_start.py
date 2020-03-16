import json

def test_hello_world(workspace):
    r = workspace.run("curl -G --data-urlencode 'greeting=Hello, World!' http://httpbin/get")
    assert json.loads(r.out)['args']['greeting'] == 'Hello, World!'
