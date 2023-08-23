const initColorPicker = (id, config) => {

  const element = document.getElementById(id);
  const colorIndicator = document.createElement('span');

  element.parentNode.style.display = 'flex';
  element.parentNode.style.alignItems = 'center';
  element.parentNode.style.position = 'relative';

  colorIndicator.style.display = 'block';
  colorIndicator.style.position = 'absolute';
  colorIndicator.style.right = '12px';
  colorIndicator.style.width = '24px';
  colorIndicator.style.height = '24px';
  colorIndicator.style.borderRadius = '50%';

  element.parentNode.appendChild(colorIndicator);

  const picker = new Pickr({
    el: element,
    useAsButton: true,
    theme: 'nano',
    default: element.value || 'white',
    swatches: [
      'rgba(244, 67, 54, 1)',
      'rgba(233, 30, 99, 0.95)',
      'rgba(156, 39, 176, 0.9)',
      'rgba(103, 58, 183, 0.85)',
      'rgba(63, 81, 181, 0.8)',
      'rgba(33, 150, 243, 0.75)',
      'rgba(3, 169, 244, 0.7)',
      'rgba(0, 188, 212, 0.7)',
      'rgba(0, 150, 136, 0.75)',
      'rgba(76, 175, 80, 0.8)',
      'rgba(139, 195, 74, 0.85)',
      'rgba(205, 220, 57, 0.9)',
      'rgba(255, 235, 59, 0.95)',
      'rgba(255, 193, 7, 1)'
    ],
    components: {
      preview: true,
      opacity: true,
      hue: true,
      interaction: {
        hex: true,
        rgba: true,
        input: true,
        clear: false,
        save: false,
      }
    }
  });

  picker
    .on('init', instance => {
      element.value = instance.getSelectedColor().toRGBA().toString(0);
      colorIndicator.style.backgroundColor = instance.getSelectedColor().toRGBA().toString(0);
    })
    .on('changestop', (source, instance) => {
      instance.applyColor(true);
      element.value = instance.getSelectedColor().toRGBA().toString(0);
      colorIndicator.style.backgroundColor = instance.getSelectedColor().toRGBA().toString(0);
      instance.hide();
    })
    .on('swatchselect', (color, instance) => {
      instance.applyColor(true);
      element.value = instance.getSelectedColor().toRGBA().toString(0);
      colorIndicator.style.backgroundColor = instance.getSelectedColor().toRGBA().toString(0);
      instance.hide();
    })
  ;

}

window.initColorPicker = initColorPicker;