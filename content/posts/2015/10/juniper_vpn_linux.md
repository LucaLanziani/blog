Title: Juniper vpn on linux!
Date: 2015-10-26 14:05
Category: Tricks
Tags: vpn, linux, juniper, 32bit
Email: luca@lanziani.com


Are you running a 64bit linux flavor and you are having problem to connect to a Juniper vpn system, even using a 32bit firefox with a 32bit jre plugin as many online pages suggest?

I have the solution of you, it is [openconnect](1):

```
sudo openconnect --juniper https://endpoint
```

that is it, wasn't it simple? ;).
 
[1]: http://www.infradead.org/openconnect/index.html
