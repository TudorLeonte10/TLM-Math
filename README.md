# TLM-Math
Proiect realizat de Leonte Tudor, Maciuc Mihai si Arama Luigi Emanuel

TLM-Math este o aplicație web dezvoltată cu Flask, organizată pe arhitectură MVC, ce oferă operații matematice (putere, factorial, Fibonacci) prin API-uri securizate cu JWT. Utilizatorii pot accesa funcționalitățile printr-un dashboard web, cu interfață modernă, iar accesul la rute este controlat în funcție de rol (ex: admin, user).

## Structură
- **app/services/**: logica matematică (power, factorial, fibonacci)
- **app/controllers/**: controlere pentru API, validare și răspunsuri
- **app/schemas/**: validare request/response cu Pydantic
- **app/middleware/**: autentificare și control acces cu JWT
- **app/templates/**: interfață web

## Funcționalități
- API REST pentru operații matematice
- Autentificare JWT și control roluri
- Salvare operații în baza de date
- Dashboard web interactiv

## Tehnologii
- Python, Flask, Pydantic, JWT

!! Din cauza unor probleme tehnice dar si prin conventie cu echipa, varianta finala a proiectului se afla pe branch-ul dockerus !!
