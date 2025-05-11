var dateElements = document.getElementsByClassName('date-format');

for (var i = 0; i < dateElements.length; i++) {
  var dateElement = dateElements[i];
  var dateTime = dateElement.textContent;

  if (dateTime) {
		var date = new Date(dateTime);

	if (!isNaN(date)) {
	  var formattedDate = date.toLocaleDateString('pt-BR', {
		day: '2-digit',
		month: '2-digit',
		year: 'numeric',
		hour: '2-digit',
		minute: '2-digit',
	  });

	  formattedDate = formattedDate.replace(',', '');	  
	  dateElement.textContent = formattedDate;
	}
  }
}