import inkex
import datetime
import re
from inkex.localization import inkex_gettext as _

class AdjustStrokeWidth(inkex.EffectExtension):
    def __init__(self):
        inkex.EffectExtension.__init__(self)
        self.arg_parser.add_argument("--lower_limit", type=float, dest="lower_limit", default=0.7, help=_("Lower stroke width limit"))
        self.arg_parser.add_argument("--upper_limit", type=float, dest="upper_limit", default=1.0, help=_("Upper stroke width limit"))
        self.arg_parser.add_argument("--target_width", type=float, dest="target_width", default=0.8, help=_("Target stroke width"))
        self.arg_parser.add_argument(
            "--input_units",
            type=str,
            dest="input_units",
            default="mm",
            help=_("Input units (mm, px, pt, pc, cm, in)"),
        )
        self.arg_parser.add_argument(
            "--target_elements",
            type=str,
            dest="target_elements",
            default="all",
            help=_("Target elements (rect, circle, ellipse, path, all)"),
        )
        self.log_file = 'extension_log.txt'
        self.enable_logging = False

    def effect(self):
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(f"--- AdjustStrokeWidth ---\n")
                f.write(f"{datetime.datetime.now()}\n")

        # Get document units
        doc_units = self.document.getroot().get(inkex.addNS('document-units', 'inkscape'))

        # Convert input values to document units (corrected)
        lower_limit = self.svg.unittouu(str(self.options.lower_limit) + self.options.input_units)  # Remove unit= argument
        upper_limit = self.svg.unittouu(str(self.options.upper_limit) + self.options.input_units)  # Remove unit= argument
        target_width = self.svg.unittouu(str(self.options.target_width) + self.options.input_units)  # Remove unit= argument

        self.print_to_log(f"Lower limit: {lower_limit} {doc_units}")
        self.print_to_log(f"Upper limit: {upper_limit} {doc_units}")
        self.print_to_log(f"Target width: {target_width} {doc_units}")

        target_elements = self.options.target_elements.split(',')

        if target_elements == ['all']:
            elements = self.svg.xpath('//*[not(self::defs or self::namedview or self::metadata or self::script)]')
        else:
            # Construct the XPath expression with namespace
            elements_query = '|'.join([f'self::svg:{element}' for element in target_elements])
            elements = self.svg.xpath(f'//*[{elements_query}]', namespaces=inkex.NSS)

        for element in elements:
            try:
                style = element.get('style')
                if style:
                    # Extract stroke-width using a regular expression
                    match = re.search(r"stroke-width:([0-9.]+)", style)  # No need to capture units
                    if match:
                        stroke_width = float(match.group(1))  # Directly convert to float
                        if lower_limit <= stroke_width <= upper_limit:
                            new_style = style.replace(f'stroke-width:{stroke_width}', f'stroke-width:{target_width}')
                            element.set('style', new_style)
                            self.print_to_log(f"Adjusted stroke width of element {element.get('id')}")
                        else:
                            self.print_to_log(f"Stroke width: {stroke_width} {doc_units} of element {element.get('id')} not in range")
                    else:
                        self.print_to_log(f"Element {element.get('id')} has no stroke-width in style attribute")
                else:
                    self.print_to_log(f"Element {element.get('id')} has no style attribute")
            except (IndexError, AttributeError):
                self.print_to_log(f"Error processing element {element.get('id')}")

        # Apply changes to the SVG document
        self.document.write(self.options.input_file)

        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write('\n\n')

    def print_to_log(self, message):
        """Prints a message to the log file if logging is enabled."""
        if self.enable_logging:
            with open(self.log_file, 'a') as f:
                f.write(message + '\n')

if __name__ == '__main__':
    AdjustStrokeWidth().run()
