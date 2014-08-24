function post_to_url(path, params, method) {
	method = method || "post";
	// Set method to post by default, if not specified.
	// The rest of this code assumes you are not using a library.
	// It can be made less wordy if you use one.
	var form = document.createElement("form");
	form.setAttribute("method", method);
	form.setAttribute("action", path);
	for(var key in params) {
		var hiddenField = document.createElement("input");
		hiddenField.setAttribute("type", "hidden");
		hiddenField.setAttribute("name", key);
		hiddenField.setAttribute("value", params[key]);
		form.appendChild(hiddenField);
	}
	document.body.appendChild(form);
	form.submit();
}

function fblogin() {
	var name;
	var img_url;
	var link;
	FB.api('/me', function (response) {
		name = response.name;
		link = response.link;
		FB.api('/me/picture?width=35&height=35', function (response) {
			img_url = response.data.url;
			$.ajax({
				url: "/login",
				dataType: 'JSON',
				data: {
					name_data: name,
					img_url: img_url,
					link_url: link
				},
				success: function (data) {
					post_to_url('/chat', {'chat_id':data.chat_id});
				}
			});
		});
	});
}

$(document).ready(function () {
	$('#facebook-btn').click(function () {
		FB.login(function(response){
			fblogin();
		});
	});
});