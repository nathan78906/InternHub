var links = Array.prototype.slice.call(document.querySelectorAll(".navbar-nav li a"));
links.push(document.querySelector(".navbar-inverse .navbar-brand"));

for (var i = 0; i < links.length; i++) {
	links[i].addEventListener("mouseover", function() {
		this.classList.add("selected");
	});
	links[i].addEventListener("mouseout", function(){
		this.classList.remove("selected");
	});
};

var RPlinks = document.querySelectorAll("td");

for (var i = 0; i < RPlinks.length; i++) {
	RPlinks[i].addEventListener("mouseover", function() {
		this.classList.add("rpselected");
	});
	RPlinks[i].addEventListener("mouseout", function() {
		this.classList.remove("rpselected");
	});
};