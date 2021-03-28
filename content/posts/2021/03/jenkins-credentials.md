Title: Jenkins Credentials
Date: 2021-03-28 21:28
Category: general, jenkins, secrets
Tags: devops, jenkins
Email: luca@lanziani.com

Snippet to get back credentials from a jenkins server.

Get to `https://jenkins-url.com/script` and paste the code below:

```groovy
import org.jenkinsci.plugins.plaincredentials.impl.*;
import com.cloudbees.plugins.credentials.impl.*;

credIds = [ "secret", "username_id" ];

(com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
    StringCredentialsImpl.class,
    Jenkins.getInstance()
) + com.cloudbees.plugins.credentials.CredentialsProvider.lookupCredentials(
    UsernamePasswordCredentialsImpl.class,
    Jenkins.getInstance()
)).each {
  print "credId: ${it.id} => ";
  if (it.id in credIds) {
    if (it.metaClass.respondsTo(it, 'getSecret')) {
        print it.getSecret();
    }

    if (it.metaClass.respondsTo(it, 'getPassword')) {
        print it.getPassword();
    }
  }
  println "";
}
```

First run will list all credentials Ids.  
Add credentials on the `credIds` list to print out the corresponding secrets.