from manim import *

class Proof(Scene):
    def construct(self):
        title1 = Tex("Hola profe, esto está hecho con \\\\"
                     "el poder de \\LaTeX y Manim.")
        self.play(Write(title1));
        self.wait()
        
        title2 = Tex("Con esto puedo hacer\\\\" "fórmulas", tex_to_color_map={"fórmulas": YELLOW})
        title2.to_corner(UP + LEFT)
        formula2 = MathTex("\\frac{a}{b} = \\frac{a+b}{a}")
        formula2.scale(2)
        self.play(Transform(title1, title2))
        self.wait()
        self.play(Write(formula2))
        self.wait()

        title3 = Tex("Con esto puedo hacer\\\\" "secuencias", tex_to_color_map={"secuencias": BLUE})
        title3.to_corner(UP + LEFT)
        sequence3 = MathTex("0,","1,","1,","2,","3,","5,","8,","13,","21,","34,","...")
        annotation3 = Tex("Y puedo señalar cosas", tex_to_color_map={"señalar": YELLOW})
        annotation3.to_corner(DOWN + RIGHT)
        annotation3.scale(0.8)
        framebox3 = SurroundingRectangle(sequence3[3], buff = .1)
        nextFramebox3 = SurroundingRectangle(sequence3[4], buff = .1)
        self.play(
            Transform(title1, title3),
            FadeOut(formula2),
        )
        self.play(Write(sequence3))
        self.wait()
        
        self.play(
            Write(annotation3),
            ShowCreation(framebox3),
            ShowCreation(nextFramebox3),
        )
        framebox32 = SurroundingRectangle(sequence3[4], buff = .1)
        nextFramebox32 = SurroundingRectangle(sequence3[5], buff = .1)
        self.play(
            ReplacementTransform(framebox3, framebox32),
            ReplacementTransform(nextFramebox3, nextFramebox32),
        )
        self.wait()
        self.play(
            FadeOut(framebox32),
            FadeOut(nextFramebox32),
            FadeOut(annotation3),
        )
        self.wait()

        title4 = Tex("Con esto puedo hacer \\\\" "dibujos", tex_to_color_map={"dibujos": BLUE})
        title4.to_corner(UP + LEFT)
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)
        
        self.play(
            Transform(title1, title4),
            FadeOut(sequence3),
        )
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
        self.wait()

        title5 = Tex("Esta librería está \\\\"
                     "muy mal documentada",
                     tex_to_color_map={"mal documentada": RED})
        self.play(
            FadeOut(title1),
            Write(title5),
        )
        self.wait()

        title6 = Tex("Pero averiguar no cuesta nada :)", tex_to_color_map={"no cuesta nada": BLUE})
        self.play(Transform(title5, title6))
        self.wait()
