Title: [Ita] Nodejs - uncaught exceptions
Date: 2012-03-14 19:35
Category: Tutorial
Tags: Nodejs, it
Email: luca@lanziani.com
Series: NodeInPillole

**Le interruzioni di servizio potrebbe essere problematiche?**

Meglio non dimenticarsi un:

	:::javascript
	process.on('uncaughtException', function (err) {
	  console.log('Caught exception: ' + err);
	});

questo garantisce che il vostro sistema continui a funzionare anche in caso di eventi inattesi.
Potrebbe salvarvi la vita diverse volte, soprattutto in produzione.

PS. Continuate a gestire in maniera corretta le eccezioni, il codice sopra è utile solo come paracadute di emergenza ;).