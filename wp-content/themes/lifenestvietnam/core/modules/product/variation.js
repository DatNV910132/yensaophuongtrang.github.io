'use strict';

jQuery(document).ready(function($) {

    $(document).on('click touch mouseover', '.product-variations', function() {
        $(this).attr('data-click', 1);
    });

    $('body').on('click', '.product-variation-radio:not(.disable-item)', function() {
        var _this = $(this);
        var _variations = _this.closest('.product-variations');
        var _click = parseInt(_variations.attr('data-click'));
        var _variations_form = _this.closest('.variations_form');

        var _id = _this.data("id");
        $('.variations_trigger .product-variation .product-variation-selector [type="radio"]' ).prop('checked', false);
        $('.variations_trigger .product-variation[data-id="' + _id + '"] .product-variation-selector [type="radio"]' ).prop('checked', true);

        product_do_select(_this, _variations, _variations_form, _click);

        _this.find('input[type="radio"]').prop('checked', true);
    });

    $('body').on('change', '.product-variation-select', function() {
        var _this = $(this);
        var _variations = _this.closest('.product-variations');
        var _click = parseInt(_variations.attr('data-click'));
        var _variations_form = _this.closest('.variations_form');
        var _selected = $('option:selected', this);

        product_do_select(_selected, _variations, _variations_form, _click);

        if (_selected.attr('data-imagesrc') !== '') {
            _this.closest('.product-variation').
            find('.product-variation-image').
            html('<img src="' + _selected.attr('data-imagesrc') + '"/>');
        } else {
            _this.closest('.product-variation').
            find('.product-variation-image').
            html('');
        }

        _this.closest('.product-variation').
        find('.product-variation-price').
        html(_selected.attr('data-pricehtml'));
    });

    if( $(".variations_trigger .product-variation").length ) {
        $("body").on("click", ".variations_trigger .product-variation", function(){
            var _id = $(this).data("id");
            $('form.add-to-cart.variations_form .product-variation[data-id="' + _id + '"]' ).trigger( "click" );
        })
    }
});


function product_do_select(selected, variations, variations_form, click) {
    if (click > 0) {
        if (!variations.closest('.wpc_variations_form').length) {
            variations_form.find('.reset_variations').trigger('click');

            if (selected.attr('data-attrs') !== '') {
                var attrs = jQuery.parseJSON(selected.attr('data-attrs'));

                if (attrs !== null) {
                    for (var key in attrs) {
                        variations_form.find('select[name="' + key + '"]').
                        val(attrs[key]).
                        trigger('change');
                    }
                }
            }
        }
    }

    jQuery(document).
    trigger('product_selected', [selected, variations, variations_form]);
}