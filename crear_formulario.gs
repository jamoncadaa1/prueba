/**
 * Enquête sur les émotions - Français IV
 * Belmer Carvajal et Julian Moncada
 *
 * Crée le formulaire Google Forms complet (4 questions, 3 réponses chacune,
 * 4 résultats dans le message de confirmation).
 * Mode d'emploi : script.google.com > Nouveau projet > coller ce code >
 * choisir la fonction crearFormulario > Exécuter > autoriser > lire le journal.
 */
function crearFormulario() {
  var form = FormApp.create('Comment te sens-tu à la fac ?');

  form.setDescription(
    'Enquête sur les émotions - Français IV\n' +
    'Par Belmer Carvajal et Julian Moncada\n\n' +
    'Lis chaque situation et choisis la réponse qui te ressemble le plus. ' +
    'Note tes lettres (A, B ou C), puis compte-les. Les résultats apparaissent ' +
    'quand tu envoies le formulaire.'
  );
  form.setProgressBar(false);
  form.setShowLinkToRespondAgain(true);

  var preguntas = [
    {
      t: 'Comment te sens-tu à la fac quand tu as un examen important la semaine prochaine ?',
      r: [
        'A) Tu te sens très stressé(e) et tu dors mal.',
        'B) Tu te sens découragé(e) et tu penses que tu vas échouer.',
        'C) Tu te sens calme et tu fais un plan pour réviser.'
      ]
    },
    {
      t: 'Comment te sens-tu à la fac quand un professeur te pose une question devant toute la classe ?',
      r: [
        'A) Tu es nerveux(se) et tu as peur de dire une bêtise.',
        'B) Tu te sens gêné(e) et tu préfères ne pas répondre.',
        'C) Tu te sens à l’aise et tu réponds avec confiance.'
      ]
    },
    {
      t: 'Comment te sens-tu à la fac quand tu dois faire un travail de groupe avec des camarades que tu ne connais pas ?',
      r: [
        'A) Tu te sens énervé(e) et tu préfères tout faire tout(e) seul(e).',
        'B) Tu te sens timide et tu restes silencieux(se) pendant la réunion.',
        'C) Tu te sens content(e) et tu proposes tout de suite des idées.'
      ]
    },
    {
      t: 'Comment te sens-tu à la fac quand tu reçois une note plus basse que prévu ?',
      r: [
        'A) Tu es furieux(se) et tu penses que le professeur n’est pas juste.',
        'B) Tu es triste et tu perds ta motivation.',
        'C) Tu es déçu(e), mais tu demandes au professeur comment progresser.'
      ]
    }
  ];

  preguntas.forEach(function (p, i) {
    form.addMultipleChoiceItem()
      .setTitle((i + 1) + '. ' + p.t)
      .setChoiceValues(p.r)
      .setRequired(true);
  });

  form.setConfirmationMessage(
    'Merci ! Compte tes lettres. Il te faut au moins 3 réponses identiques sur 4 pour avoir un résultat « surtout ».\n\n' +
    'Tu as surtout répondu C ?\n' +
    'La fac se passe bien pour toi ! Tu restes calme, tu gardes confiance en toi et tu cherches des solutions quand il y a un problème. Continue comme ça et n’hésite pas à aider tes camarades quand ils sont stressés.\n\n' +
    'Tu as surtout répondu A ?\n' +
    'Attention ! Tu vis la fac avec beaucoup de stress et de colère. Tes émotions sont fortes et elles te fatiguent. Respire avant de réagir, fais une pause ou une activité physique, et parle de ce qui t’énerve avec quelqu’un de confiance.\n\n' +
    'Tu as surtout répondu B ?\n' +
    'Tu sembles parfois triste ou découragé(e) à la fac, et tu préfères rester en retrait. Ce n’est pas grave, mais ne reste pas seul(e) avec ces émotions. Fixe-toi de petits objectifs, parle avec un ami ou un professeur et demande de l’aide quand tu en as besoin.\n\n' +
    'Tes réponses sont très variées ?\n' +
    'Tes émotions changent selon la situation, et c’est normal. Tu es calme dans certains moments et plus fragile dans d’autres. Observe quelles situations te stressent ou te découragent le plus, et prépare une petite stratégie pour chacune.'
  );

  Logger.log('Lien pour répondre : ' + form.getPublishedUrl());
  Logger.log('Lien pour modifier : ' + form.getEditUrl());
}
