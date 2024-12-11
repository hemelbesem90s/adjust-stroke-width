# Inkscape Adjust Stroke Width Extension

This extension allows you to adjust the stroke width of selected elements in an Inkscape document based on specified criteria.

## Functionality

The extension provides a dialog box where you can:

* Set the lower and upper limits for the stroke width (in millimeters).
* Set the desired target stroke width (in millimeters).
* Select the types of elements to target (rect, circle, ellipse, path, or all).

The extension then iterates through the selected elements and adjusts the stroke width of those that fall within the specified limits to the target width.

## Usage

1. Install the extension by placing the `adjust_stroke_width.inx` and `adjust_stroke_width.py` files in your Inkscape extensions directory.
2. Open your SVG document in Inkscape.
3. Go to `Extensions > Object > Adjust Stroke Width`.
4. In the dialog box, set the lower and upper limits for the stroke width, the target width, and the types of elements to target.
5. Click "Apply".

## Options

The extension provides the following options:

* **Lower limit:** The lower limit for the stroke width (in millimeters).
* **Upper limit:** The upper limit for the stroke width (in millimeters).
* **Target width:** The desired stroke width (in millimeters) for elements that fall within the specified limits.
* **Target elements:** The types of elements to target (rect, circle, ellipse, path, or all).

## Acknowledgements

This extension was developed with the help of [Gemini Advanced](https://sites.research.google/gemini), Google's next-generation AI model. 

Special thanks to the Inkscape community for their valuable contributions and support, particularly the following resources:

* Inkscape Forum: [https://inkscape.org/forums/](https://inkscape.org/forums/)
* Inkscape Wiki: [https://wiki.inkscape.org/wiki/](https://wiki.inkscape.org/wiki/)
* Inkscape Extensions Documentation: [https://inkscape.gitlab.io/extensions/documentation/](https://inkscape.gitlab.io/extensions/documentation/)

## License

This extension is licensed under the GNU General Public License v2.0. See the LICENSE file for details.
