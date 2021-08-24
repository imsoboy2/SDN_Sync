for i in range(1, 5001):
    filename = "flow_br0_in_p2_out_p1_%d.json" % i
    with open(filename, "w") as f:
        data = ''' {
  "flows": [
    {
      "priority": "%d",
      "timeout": 1,
      "isPermanent": false,
      "deviceId": "of:0000daeaadf8c24e",
      "treatment": {
        "instructions": [
          {
            "type": "OUTPUT",
            "port": "1"
          }
        ]
      },
      "selector": {
        "criteria": [
          {
            "type": "IN_PORT",
            "port": "2"
          }
        ]
      }
    }
  ]
}'''
        f.write(data)
