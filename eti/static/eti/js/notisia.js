/*
Normaliza hau nia code nune'e iha tempu naruk hau husik tiha projetu ida ne'e. nune'e hau hare fila fali code hirak nee hau komrende ho diak
*/

// ida hodi kaer div ho class="news-container"
const newsContainer = document.querySelector('.news-container');

// deklara function ida hodi truncate string sira
// minimiza 100 character husi string
function truncateString(str, maxLength) {
  if (str.length > maxLength) {
    return str.substring(0, maxLength) + "...";
  } else {
    return str;
  }
}

// variable hirak nee kolabora ho function 'truncateString'
let str = "";
let maxLength = 100;
let truncatedStr = "";


let existNews = "";
// function ida nee hodi foti dadus notisia hotu-hotu iha http://127.0.0.1:8000/api/news/ i depois uja method array.shift() hodi hetan dadus primeiru ho index 0 no hatama ba variable 'existNews'
// ho nunee ikus mai hodi halo logica hetan dadus foun husi notisia
function getAllData() {
  newsContainer.innerHTML = "";

  fetch('http://127.0.0.1:8000/api/notisias/')
    .then(resp => resp.json())
    .then(allNews => {
      allNews.forEach(news => {
        str = news.content;
        truncatedStr = truncateString(str, maxLength);

        newsContainer.insertAdjacentHTML('beforeend', `  
          <div class="col-sm-4 card p-0 m-3" style="width: 18.75em" data-url="${news.url}">
            <img src="${news.img}" class="card-img-top placeholder" alt="..." style="height: 250px; object-fit: cover" />
            <div class="card-body placeholder-wave">
            <h5 class="card-title placeholder">${news.titulu}</h5>
            <p class="card-text placeholder">${truncatedStr}</p>
            <a href="/notisia/${news.id}/" class="btn btn-primary placeholder">Lee liu tan</a>
          </div>
        </div>
        `);

        const pGlow = document.querySelectorAll('.placeholder-wave');
        const p = document.querySelectorAll('.placeholder');

        setTimeout(() => {
          pGlow.forEach(el => el.classList.remove('placeholder-wave'));
          p.forEach(el => el.classList.remove('placeholder'));
        }, 250);
      });

      existNews = allNews.shift(); // shif here!
    });
}
getAllData();

// hetan dadus husi notisia kada 5 segundu
// no halo komparasaun ba dadus primeiru hodi nune'e bele hetan dadus foin ne'ebe maka husi notisia no update ba iha frontend
function getNewData() {

  fetch('http://127.0.0.1:8000/api/notisias/')
    .then(resp => resp.json())
    .then(allNews => {
      const news = allNews.shift();

      if (!(news["url"] === existNews["url"])) {

        newsContainer.insertAdjacentHTML('afterbegin', `
          <div class="col-sm-4 card p-0 m-3" style="width: 18.75em" data-url="${news.url}">
            <img src="${news.img}" class="card-img-top placeholder" alt="..." style="height: 250px; object-fit: cover" />
            <div class="card-body placeholder-wave">
              <h5 class="card-title placeholder">${news.titutlu}</h5>
              <p class="card-text placeholder">${truncatedStr}</p>
              <a href="/notisia/${news.id}/" class="btn btn-primary placeholder">Lee liu tan</a>
            </div>
          </div>
        `);

        const pGlow = document.querySelectorAll('.placeholder-wave');
        const p = document.querySelectorAll('.placeholder');

        setTimeout(() => {
          pGlow.forEach(el => el.classList.remove('placeholder-wave'));
          p.forEach(el => el.classList.remove('placeholder'));
        }, 250);
      } else {
        console.log("Data exist!");
      }
      // reassign existing news
      existNews = news;

    });

  setTimeout(getNewData, 5000); // 5000 milliseconds equals to 5 seconds
}
getNewData();

// buka dadus ho asynchronous bazeadu ho javascript
// no seidauk utiliza endpoint search ho backend 'django_filters'
// maibe iha possibilidade atu troka ba 'django_filters' hodi buka dadus diak liu tan

// kaer input tag ho id="news-search"
const newsSearch = document.querySelector("#news-search");

// asynchronous buka dadus realtime ou autocomplete iha nee
// ho bainhira ita hanehan no husik keyboard
newsSearch.addEventListener('keyup', async (e) => {
  e.preventDefault();

  const x = await fetch('http://127.0.0.1:8000/api/notisias/');
  const allNews = await x.json();

  const keyword = e.target.value.toLowerCase().trim();
  if (keyword === "") {
    getAllData();
    return;
  }

  const matchNews = allNews.filter(news => {
    return news.titulu.toLowerCase().includes(keyword);
  });

  updateNewsWithSearch(matchNews, keyword);

});

// function ida nee hodi hatudu rezultadu ba iha frontend
// ho meius rezultadu user buka iha search input
function updateNewsWithSearch(data, keyword) {

  newsContainer.innerHTML = "";

  if (JSON.stringify(data) === "[]") {
    const div = document.createElement("div");
    div.className = "col-12 text-start text-dark";
    div.textContent = `
    La hetan "${keyword}"!
    `;
    newsContainer.appendChild(div);
    return;
  }

  data.forEach(news => {

    newsContainer.innerHTML += `
      <div class="col-sm-4 card p-0 m-3" style="width: 18.75em" data-url="${news.url}">
        <img src="${news.img}" class="card-img-top placeholder" alt="..." style="height: 250px; object-fit: cover" />
        <div class="card-body placeholder-wave">
          <h5 class="card-title placeholder">${news.titulu}</h5>
          <p class="card-text placeholder">${truncatedStr}</p>
          <a href="/notisia/${news.id}/" class="btn btn-primary placeholder">Lee liu tan</a>
        </div>
      </div>
    `;

    const pGlow = document.querySelectorAll('.placeholder-wave');
    const p = document.querySelectorAll('.placeholder');

    setTimeout(() => {
      pGlow.forEach(el => el.classList.remove('placeholder-wave'));
      p.forEach(el => el.classList.remove('placeholder'));
    }, 250);

  });

}

// detecta karik data iha server hamoos
// entaun iha frontend mos hasai tiha / remove ho JavaScript
function removeNewsIfDoestNotExist() {
  fetch('http://127.0.0.1:8000/api/notisias/')
    .then(resp => resp.json())
    .then(allNews => {

      const divUrl = document.querySelectorAll("div[data-url]");

      divUrl.forEach(div => {
        const url = div.dataset.url;

        const existInData = allNews.some(data => data.url === url);

        if (!existInData) {
          div.remove();
        }
      });
    });

  setTimeout(removeNewsIfDoestNotExist, 5000);
}

removeNewsIfDoestNotExist();