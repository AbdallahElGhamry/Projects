function user_kernel(src, event ,uit, dlg)
            global user_mask;
            user_mask = get(uit, 'data');
            delete(dlg);
end