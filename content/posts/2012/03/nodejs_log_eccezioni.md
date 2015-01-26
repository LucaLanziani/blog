Title: [Ita] Nodejs - log eccezioni inattese
Date: 2012-03-15 20:35
Category: Tutorial
Tags: Nodejs, it
Email: luca@lanziani.com
Series: NodeInPillole
Lang: it

Nella pillola precedente [(uncaught exception)][1] abbiamo visto come evitare interruzioni inaspettate del servizio.

E’ opportuno tenere un log di questi eventi in modo da correggere gli errori che li hanno scatenati, sostituendo il console.log dell’esempio precedente con qualcosa di simile a:

	:::javascript
	var date = new Date();
	console.error("Eccezione inattesa: il %s\n %s", date.toLocaleString(), err.stack);

magari re-direzionando lo stderr in un file.

Unix tip:

	:::bash
	node app.js 2> error.log

[1]: /ita-nodejs-uncaught-exceptions.html