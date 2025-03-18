const studenti = [
  { ime: "Marko", prezime: "Petrović", godina: 3, ocjene: [9, 8, 7, 10, 9] },
  { ime: "Ana", prezime: "Jovanović", godina: 1, ocjene: [7, 6, 8, 6, 7] },
  { ime: "Luka", prezime: "Simić", godina: 2, ocjene: [10, 9, 10, 8, 9] },
  { ime: "Maja", prezime: "Nikolić", godina: 4, ocjene: [6, 5, 7, 6, 6] },
  { ime: "Ivana", prezime: "Stanković", godina: 1, ocjene: [9, 10, 9, 8, 9] },
];
function prosjek(ocjene) {
  let suma = 0;
  for (let i = 0; i < ocjene.length; i++) {
    suma += ocjene[i];
  }
  return suma / ocjene.length;
}

function checkStudent(studenti) {
  let output = [];
  for (let i = 0; i < studenti.length; i++) {
    if (prosjek(studenti[i].ocjene) > 8.5) output.push(studenti[i]);
    else output.push(studenti[i].ime);
  }
  return output;
}

function theBest(studenti) {
  let maximum = 0;
  let best;
  for (let i = 0; i < studenti.length; i++) {
    if (prosjek(studenti[i].ocjene) > maximum) {
      best = studenti[i];
      maximum = prosjek(studenti[i].ocjene);
    }
  }

  return best;
}

function prosjekProsjeka(studenti) {
  let suma = 0;
  for (let i = 0; i < studenti.length; i++) {
    suma += prosjek(studenti[i].ocjene);
  }
  return suma / studenti.length;
}

function bubbleSort(studenti) {
  let studentiCopy = [...studenti];

  for (let i = 0; i < studentiCopy.length - 1; i++) {
    for (let j = 0; j < studentiCopy.length - i - 1; j++) {
      if (
        prosjek(studentiCopy[j].ocjene) < prosjek(studentiCopy[j + 1].ocjene)
      ) {
        let temp = studentiCopy[j];
        studentiCopy[j] = studentiCopy[j + 1];
        studentiCopy[j + 1] = temp;
      }
    }
  }

  return studentiCopy;
}
function updateProsjek(studenti) {
  for (let i = 0; i < studenti.length; i++) {
    studenti[i].prosjek = prosjek(studenti[i].ocjene);
  }
}

updateProsjek(studenti);

console.log(
  checkStudent(studenti),
  theBest(studenti),
  prosjekProsjeka(studenti),
  bubbleSort(studenti)
);

theBest(studenti);
