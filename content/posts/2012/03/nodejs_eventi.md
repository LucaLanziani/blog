Title: [Ita] Nodejs - gli eventi
Date: 2012-03-06 19:20
Category: Tutorial
Tags: Nodejs, it
Email: luca@lanziani.com
Series: NodeInPillole
Lang: it

Abbiamo citato il fatto che un punto di forza di nodejs è dato dal suo essere guidato da eventi.
Vediamo quindi come agganciare una callback agli eventi.

{% youtube ZF7toA0FLGI %}

Il [sito ufficiale]( http://nodejs.org/about/) ci dice che, nell’esempio del server web “hello world”, node chiede al sistema operativo di notificagli ogni nuova connessione prima di mettersi in sleep.
Quando si verifica una nuova connessione node esegue la callback associata all’evento.

