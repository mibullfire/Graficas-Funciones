f(x) = 'ecuacion'
#include <stdio.h>
#include <math.h>
#include <cairo/cairo.h>

void draw_graph() {
    int width = 640;
    int height = 480;
    cairo_surface_t *surface = cairo_image_surface_create(CAIRO_FORMAT_ARGB32, width, height);
    cairo_t *cr = cairo_create(surface);

    // Set background color
    cairo_set_source_rgb(cr, 1, 1, 1);
    cairo_paint(cr);

    // Draw axes
    cairo_set_source_rgb(cr, 0, 0, 0);
    cairo_set_line_width(cr, 2);
    cairo_move_to(cr, 50, height / 2);
    cairo_line_to(cr, width - 50, height / 2);
    cairo_move_to(cr, width / 2, 50);
    cairo_line_to(cr, width / 2, height - 50);
    cairo_stroke(cr);

    // Draw graph of f(x) = x^2
    cairo_set_source_rgb(cr, 1, 0, 0);
    cairo_set_line_width(cr, 1);
    for (double x = -10; x <= 10; x += 0.1) {
        double y = x * x;
        double x_pos = width / 2 + x * 20;
        double y_pos = height / 2 - y * 20;
        if (x == -10) {
            cairo_move_to(cr, x_pos, y_pos);
        } else {
            cairo_line_to(cr, x_pos, y_pos);
        }
    }
    cairo_stroke(cr);

    // Save the image to a file
    cairo_surface_write_to_png(surface, "graph.png");

    // Clean up
    cairo_destroy(cr);
    cairo_surface_destroy(surface);
}

int main() {
    draw_graph();
    return 0;
}