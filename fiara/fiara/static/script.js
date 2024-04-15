<script>
    $('#modalModifier').on('show.bs.modal', function (event) {
        var button = $(event.relatedTarget); // Button that triggered the modal
        var id = button.data('id'); // Extract info from data-* attributes
        var modal = $(this);

        // Make an AJAX request to fetch the details of the selected person
        $.ajax({
            url: '/fetch-personne/' + id + '/', // Assuming you have a URL to fetch person details
            type: 'GET',
            success: function (data) {
                // Assuming data contains JSON with person details
                modal.find('#idPersonne').val(data.id);
                modal.find('#nomModifier').val(data.nom);
                modal.find('#prenomModifier').val(data.prenom);
                modal.find('#ageModifier').val(data.age);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
</script>