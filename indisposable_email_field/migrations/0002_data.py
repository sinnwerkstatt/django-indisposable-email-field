# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

from indisposable_email_field.models import DisposableDomainName

domain_names = ['0clickemail.com', 'noclickemail.com', '10minutemail.com', 'bofthew.com', 'drdrb.com', 'drdrb.net',
                'jnxjn.com', 'klzlk.com', 'nepwk.com', 'nwldx.com', 'owlpic.com', 'pjjkp.com', 'prtnx.com', 'rmqkr.net',
                'rppkn.com', 'rtrtr.com', 'trbvm.com', 'tyldd.com', 'uggsrock.com', '10minutemail.net', 'akerd.com',
                'soisz.com', 'zoaxe.com', '12houremail.com', '12minutemail.com', '1pad.de', '20minutemail.com',
                '30minutenmail.eu', '5ymail.com', '60-minuten-mail.de', 'akapost.com', 'anon-mail.de', 'anonbox.net',
                'anonmails.de', 'anonymbox.com', 'anonymous-email.net', 'anonymousfeedback.net', 'antispam.de',
                'antispam24.de', 'antispammail.de', 'b2cmail.de', 'breakthru.com', 'bspamfree.org', 'bugmenot.com',
                'bumpymail.com', 'byom.de', 'trashmail.org', 'cam4you.cc', 'centermail.com', 'centermail.net',
                'deadaddress.com', 'despammed.com', 'dispostable.com', 'dodgeit.com', 'dodgit.com', 'dontsendmespam.de',
                'dotman.de', 'dudmail.com', 'dump-email.info', 'dumpmail.de', 'e4ward.com', 'easytrashmail.com',
                'edv.to', 'einfach.to', 'eintagsmail.de', 'emailgo.de', 'emailias.com', 'emailsensei.com',
                'emailtemporanea.com', 'emailtemporanea.net', 'empiremail.de', 'eyepaste.com', 'fakeinbox.com',
                'fakemail.fr', 'adresseemailtemporaire.com', 'armyspy.com', 'cuvox.de', 'dayrep.com', 'einrot.com',
                'fakemailgenerator.com', 'fleckens.hu', 'gustr.com', 'jourrapide.com', 'rhyta.com', 'superrito.com',
                'teleworm.us', 'wegwerfemailadresse.com', 'filzmail.com', 'flitafir.de', 'frapmail.com',
                'garbagemail.org', 'garliclife.com', '7tags.com', 'broadbandninja.com', 'cellurl.com', 'dealja.com',
                'getairmail.com', 'moburl.com', 'tagyourself.com', 'vidchart.com', 'getmails.eu', 'consumerriot.com',
                'getonemail.com', 'gishpuppy.com', 'nurfuerspam.de', 'guerillamail.org', 'guerrillamail.net', 'grr.la',
                'guerrillamail.biz', 'guerrillamail.com', 'guerrillamail.de', 'guerrillamail.info', 'guerrillamail.org',
                'sharklasers.com', 'spam4.me', 'guerrillamailblock.com', 'haltospam.com', 'harakirimail.com',
                'hidemail.de', 'hidemyass.com', 'hmamail.com', 'bootybay.de', 'gehensiemirnichtaufdensack.de',
                'hat-geld.de', 'ieh-mail.de', 'plexolan.de', 'inbox.si', 'incognitomail.com', 'incognitomail.net',
                'incognitomail.org', 'instant-mail.de', 'sinnlos-mail.de', 'wegwerf-email-adressen.de',
                'wegwerf-emails.de', 'ip6.li', 'irish2me.com', 'jetable.com', 'jetable.net', 'jetable.org', 'junk.to',
                'kasmail.com', 'keepmymail.com', 'koszmail.pl', 'lhsdv.com', 'lifebyfood.com', 'lr78.com',
                'luckymail.org', 'card.zp.ua', 'express.net.ua', 'infocom.zp.ua', 'mail.zp.ua', 'mycard.net.ua',
                'mail1a.de', 'delikkt.de', 'm21.cc', 'mail21.cc', 'mysamp.de', 'mail4trash.com', 'mailcatch.com',
                'mailbiz.biz', 'mailde.de', 'mailde.info', 'mailms.com', 'mailorg.org', 'mailtv.net', 'mailtv.tv',
                'ministry-of-silly-walks.de', 'maildrop.cc', 'maileater.com', 'maileimer.de', 'mailexpire.com',
                'mailfish.de', 'mailforspam.com', 'binkmail.com', 'bobmail.info', 'chammy.info', 'chogmail.com',
                'devnullmail.com', 'letthemeatspam.com', 'mailin8r.com', 'mailinater.com', 'mailinator.com',
                'mailinator.net', 'mailinator2.com', 'mailismagic.com', 'mailtothis.com', 'monumentmail.com',
                'notmailinator.com', 'putthisInyourspamdatabase.com', 'reallymymail.com', 'safetymail.info',
                'slopsbox.com', 'sogetthis.com', 'spamgoes.in', 'spamherelots.com', 'SpamHerePlease.com',
                'supergreatmail.com', 'suremail.info', 'thisisnotmyrealemail.com', 'tradermail.info',
                'veryrealemail.com', 'zippymail.info', 'mailita.tk', 'mailme24.com', 'mailnesia.com', 'mailnull.com',
                'mailshell.com', 'mailtome.de', 'mailtrash.net', 'makemetheking.com', 'mbx.cc', 'meltmail.com',
                'messagebeamer.de', 'migmail.pl', 'mintemail.com', 'muell.email', 'my10minutemail.com',
                'mytempmail.com', 'mailmetrash.com', 'mt2009.com', 'mt2014.com', 'mytrashmail.com', 'thankyou2010.com',
                'trash2009.com', 'trashymail.com ', 'nervmich.net', 'nervtmich.net', 'wegwerfadresse.de',
                'netzidiot.de', 'no-spam.ws', 'nospam4.us', 'nospamfor.us', 'nospammail.net', 'nowmymail.com',
                'nsaking.de', 'obobbo.com', 'ohaaa.de', 'blackmarket.to', 'omail.pro', 'thc.st', 'vpn.st',
                'oneoffemail.com', 'oneoffmail.com', 'onewaymail.com', 'onlatedotcom.info', 'otherinbox.com',
                'pookmail.com', 'privacy.net', 'privatdemail.net', 'fansworldwide.de', 'privy-mail.de', 'privymail.de',
                'trashmailer.com', 'put2.net', 'quickinbox.com', 'realtyalerts.ca', 'mailseal.de', 'receiveee.com',
                'safersignup.de', 'safetypost.de', 'sapya.com', 'schafmail.de', 'schmeissweg.tk', 'schrott-email.de',
                'secretemail.de', 'lolfreak.net', 'secure-mail.biz', 'secure-mail.cc', 'z1p.biz', 'send-email.org',
                'SendSpamHere.com', 'senseless-entertainment.com', 'is.af', 'server.ms', 'us.af', 'shieldemail.com',
                'sneakemail.com', 'snkmail.com', 'sofort-mail.de', 'sofortmail.de', 'soodonims.com', 'spam.la',
                'spam.su', 'spamail.de', 'spamavert.com', 'spambob.com', '0815.ru', '3d-painting.com', '6ip.us',
                'agedmail.com', 'ama-trade.de', 'ama-trans.de', 'ano-mail.net', 'bio-muesli.info', 'bio-muesli.net',
                'brennendesreich.de', 'buffemail.com', 'bund.us', 'cust.in', 'dbunker.com', 'discardmail.com',
                'discardmail.de', 'dropcake.de', 'duskmail.com', 'e-postkasten.com', 'e-postkasten.de',
                'e-postkasten.eu', 'e-postkasten.info', 'emaillime.com', 'ero-tube.org', 'film-blog.biz', 'fly-ts.de',
                'flyspam.com', 'fr33mail.info', 'geschent.biz', 'great-host.in', 'hochsitze.com', 'hulapla.de',
                'imails.info', 'kulturbetrieb.info', 'lags.us', 'm4ilweb.info', 'malahov.de', 'misterpinball.de',
                'mypartyclip.de', 'nomail2me.com', 'nospamthanks.info', 'politikerclub.de', 'recode.me', 's0ny.net',
                'sandelf.de', 'sky-ts.de', 'spambog.com', 'spambog.de', 'spambog.ru', 'superstachel.de', 'teewars.org',
                'thanksnospam.info', 'watch-harry-potter.com', 'watchfull.net', 'webm4il.info', 'spambox.us',
                'spamcero.com', 'spamcorptastic.com', 'spamex.com', 'spamfree.eu', 'spamfree24.com', 'spamfree24.de',
                'spamfree24.info', 'spamfree24.org', 'antichef.net', 'spamcannon.net', 'spamgourmet.com',
                'spamgourmet.net', 'spamgourmet.org', 'spamhole.com', 'spaminator.de', 'spaml.de', 'spammotel.com',
                'spamobox.com', 'spamspot.com', 'SpamThisPlease.com', 'spamtrail.com', 'spamtroll.net', 'cheatmail.de',
                'dodgemail.de', 'fivemail.de', 'giantmail.de', 'nevermail.de', 'smashmail.de', 'sneakmail.de',
                'spoofmail.de', 'stuffmail.de', 'tokenmail.de', 'trialmail.de', 'squizzy.de', 'sry.li',
                'stinkefinger.net', 'sofimail.com', 'stop-my-spam.com', 'super-auswahl.de', 'teleworm.com',
                'checknew.pw', 'gomail.in', 'inboxed.im', 'inboxed.pw', 'linuxmail.so', 'nomail.pw', 'powered.name',
                'secmail.pw', 'shut.name', 'shut.ws', 'temp-mail.org', 'tokem.co', 'vipmail.name', 'vipmail.pw',
                'writeme.us', 'yanet.me', 'llogin.ru', 'odnorazovoe.ru', 'temp-mail.ru', 'tempail.com',
                'tempemail.co.za', 'tempemail.net', 'beefmilk.com', 'dingbone.com', 'fudgerub.com', 'lookugly.com',
                'smellfear.com', 'tempinbox.com', 'tempmail.eu', 'tempmailer.com', 'tempmailer.de', 'tempomail.fr',
                'temporarily.de', 'temporaryemail.net', 'temporaryinbox.com', 'temporarymailaddress.com',
                'thismail.net', 'tittbit.in', 'topranklist.de', 'tormail.org', 'fake-box.com', 'opentrash.com',
                're-gister.com', 'trash-mail.com', 'trash-mail.de', 'trash-me.com', 'you-spam.com', 'trash4.me',
                'trashdevil.com', 'trashdevil.de', 'trashemail.de', 'trashmail.com', 'trashmail.de', 'kurzepost.de',
                'objectmail.com', 'proxymail.eu', 'punkass.com', 'rcpt.at', 'trash-mail.at', 'trashmail.at',
                'trashmail.me', 'trashmail.net', 'wegwerfmail.de', 'wegwerfmail.net', 'wegwerfmail.org', 'trashmail.ws',
                'twinmail.de', '163.com', '2prong.com', '8127ep.com', 'antireg.ru', 'asdasd.ru', 'bugmenever.com',
                'despam.it', 'disposeamail.com', 'dontreg.com', 'einmalmail.de', 'fakedemail.com', 'fuckingduh.com',
                'fyii.de', 'humaility.com', 'ignoremail.com', 'kostenlosemailadresse.de', 'lawlita.com',
                'losemymail.com', 'mailscrap.com', 'nabuma.com', 'nobugmail.com', 'nobuma.com', 'pwrby.com',
                'qoika.com', 'sector2.org', 'secure-mail.cn', 'spamday.com', 'spamkill.info', 'spaml.com', 'tilien.com',
                'trashinbox.com', 'wegwerf-email.de', 'yxzx.net', 'zetmail.com', 'vsimcard.com', 'wasteland.rfc822.org',
                'weg-werf-email.de', 'wegwerf-email.net', 'wegwerfemail.com', 'wegwerfemail.de', 'wh4f.org',
                'willhackforfood.biz', 'whyspam.me', 'wolfsmail.tk', 'wolfsmails.tk', 'x.ip6.li', 'cool.fr.nf',
                'courriel.fr.nf', 'jetable.fr.nf', 'mega.zik.dj', 'moncourrier.fr.nf', 'monemail.fr.nf',
                'monmail.fr.nf', 'nomail.xl.cx', 'nospam.ze.tc', 'speed.1s.fr', 'yopmail.com', 'yopmail.fr',
                'yopmail.net', 'youmailr.com', 'zehnminuten.de', 'zehnminutenmail.de',
                ]


class Migration(SchemaMigration):
    def forwards(self, orm):
        ddns = [DisposableDomainName(value=name) for name in domain_names]
        DisposableDomainName.objects.bulk_create(ddns)

    def backwards(self, orm):
        DisposableDomainName.objects.filter(value__in=domain_names).delete()

    models = {
        u'indisposable_email_field.disposabledomainname': {
            'Meta': {'object_name': 'DisposableDomainName'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '500'})
        }
    }

    complete_apps = ['indisposable_email_field']
