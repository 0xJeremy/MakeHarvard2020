var trow = document.getElementById("trow");
var sorting = document.getElementById("sorting");

function start(type) {
	$.post("start",
	  {
	    type: type
	  },
	  function(data, status){
	    console.log("Sorting Started on " + type)
	});
}

function write_type(type) {
	sorting.innerHTML = type
}
write_type("[Not Currently Sorting]")

var started = false;

function sort_suit() {
	if(started) {
		trow.innerHTML = "ERROR! Sorting has already started."
		return;
	}
	started = true
	start("suit")
	write_type("Currently Sorting: Suit")
	trow.innerHTML = "";
}

function sort_rank() {
	if(started) {
		trow.innerHTML = "ERROR! Sorting has already started."
		return;
	}
	started = true
	start("rank")
	write_type("Currently Sorting: Rank")
	trow.innerHTML = "";

}

function stop() {
	if(!started) {
		trow.innerHTML = "ERROR! Sorting not started."
		return;
	}
	started = false;
	start("stop")
	write_type("[Not Currently Sorting]")
	trow.innerHTML = "";
}
