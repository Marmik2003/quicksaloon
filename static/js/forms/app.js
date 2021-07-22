function restrictAlphabets(e) {
    const x = e.which || e.keycode;
    return (x >= 48 && x <= 57);
}