class BaseColorPickerWidget extends window.telepath.constructors["wagtail.widgets.Widget"] {

  constructor(options) {
    super();
    this.options = options;
  }

  render(placeholder, name, id, initialState) {

    const element = document.createElement('input');

    element.type = 'text';
    element.name = name;
    element.id = id;

    placeholder.replaceWith(element);

    this.initChooserFn(id, this.options);

    const widget = {
      getValue() {
        return element.value;
      },
      getState() {
        return element.value;
      },
      setState(state) {
        element.value = state;
      },
      focus(opts) {
        // focusing opens the date picker, so don't do this if it's a 'soft' focus
        if(opts && opts.soft) return;
        element.focus();
      },
      idForLabel: id,
    };

    widget.setState(initialState);

    return widget;
  }
}

class AdminColorPickerInput extends BaseColorPickerWidget {
  initChooserFn = window.initColorPicker;
}

window.telepath.register('home.widgets.ColorPickerInput', AdminColorPickerInput);
