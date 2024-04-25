// document.addEventListener('DOMContentLoaded', function () {
//     var modalBtn = document.querySelector('.modal-btn');
//     var modal = document.getElementById('myModal');
//     var closeBtn = document.querySelector('.close');
//     var mapContainer = document.getElementById('map');
//     var map; // переменная для хранения объекта карты
//
//     // Show modal
//     modalBtn.onclick = function () {
//         modal.style.display = 'block';
//         if (!map) {
//             initMap();
//         }
//     }
//
//     // Close modal
//     closeBtn.onclick = function () {
//         modal.style.display = 'none';
//     }
//
//     // Close modal on outside click
//     window.onclick = function (e) {
//         if (e.target == modal) {
//             modal.style.display = 'none';
//         }
//     }
//
//     function initMap() {
//         ymaps.ready(function () {
//             map = new ymaps.Map('map', {
//                 center: [55.7558, 37.6173], // центр карты на Москве
//                 zoom: 12 // масштаб карты
//             });
//
//             // Добавляем обработчик клика по карте
//             map.events.add('click', function (e) {
//                 var coords = e.get('coords');
//                 getAddress(coords);
//             });
//
//             // Добавляем обработчик изменения значения в поле ввода
//             document.getElementById('search').addEventListener('input', function () {
//                 var address = document.getElementById('search').value;
//                 ymaps.geocode(address).then(function (res) {
//                     var firstGeoObject = res.geoObjects.get(0);
//                     var coords = firstGeoObject.geometry.getCoordinates();
//                     map.setCenter(coords);
//                 });
//             });
//         });
//     }
//
//     // Функция получения адреса по координатам
//     function getAddress(coords) {
//         ymaps.geocode(coords).then(function (res) {
//             var firstGeoObject = res.geoObjects.get(0);
//             var address = firstGeoObject.getAddressLine();
//             document.getElementById('search').value = address;
//         });
//     }
// });
