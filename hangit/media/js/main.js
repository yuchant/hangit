$(function() {
	$(".outfits .outfit-choice").click(function() {
		console.log("Clicked");
		$found = $(this).parent().find('option[value=' + $(this).data('id') + ']');
		// $(this).parent().find('option').prop('checked', false);
		$(this).parent().find('select').val($(this).data('id'));
		select = $(this).closest('select');

		$(this).parent().find('.active').removeClass('active');
		$(this).addClass('active');
	})
})