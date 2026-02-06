"use client";

import { Linefont } from "next/font/google";
import { useEffect, useRef } from "react";

class Point {
    x: number;
    y: number;

    constructor(nx: number, ny: number) {
        this.x = nx;
        this.y = ny;
    }
}

export default function SpellSketch() {
    const sketchRef = useRef<HTMLDivElement>(null);


    useEffect(() => {
        let p5Instance: any;

        const loadP5 = async () => {
            const p5 = (await import("p5")).default;
            let points: Point[] = []
            let b_form = "00000000101"
            let b_power = "00000001111"
            let b_shape = "00000000101"
            let b_target = "00000011001"
            let b_technique = "00000100001"

            let binary_codes : String[] = []
            binary_codes.push(b_form);
            binary_codes.push(b_power);
            binary_codes.push(b_shape);
            binary_codes.push(b_target);
            binary_codes.push(b_technique);

            let num_points = 11;

            const sketch = (p: any) => {
                p.setup = () => {
                    p.createCanvas(400, 400);

                    let center_x = p.width / 2;
                    let center_y = p.width / 2;
                    let radius = (p.width - 50) / 2;

                    for (let i = 0; i < num_points; i++) {
                        let theta = (2 * p.PI * i / num_points) - p.PI / 2;
                        let x = center_x + radius * p.cos(theta)
                        let y = center_y + radius * p.sin(theta)
                        points.push(new Point(x, y))
                    }

                    console.log(points)
                };

                p.draw = () => {
                    p.background(255);
                    p.fill(255);
                    p.strokeWeight(4);
                    p.stroke(200, 100, 100)
                    p.circle(p.width / 2, p.width / 2, p.width - 50);
                    
                    p.strokeWeight(2)
                    p.stroke(222, 222, 222)
                    for (var pt of points) {
                         for (var pt2 of points){
                            p.line(pt.x, pt.y, pt2.x, pt2.y)
                        } 
                    }
                
                    //shape
                    p.strokeWeight(3)
                    p.stroke(100, 100, 100)

                    let count = 0
                    for (var bc of binary_codes){
                        for (var i = 0; i< num_points; i++ ){
                            let xx = bc.charAt(i);
                            if (xx == '1') {
                                p.line(points[count].x, points[count].y,points[i].x, points[i].y)
                            }
                        }
                        count++;
                    }

                    p.strokeWeight(4);
                    p.stroke(200, 100, 100)
                    for (var pt of points) {
                        p.stroke(200, 100, 100)
                        p.circle(pt.x, pt.y, 20)
                    }
                };
            };

            if (sketchRef.current) {
                p5Instance = new p5(sketch, sketchRef.current);
            }
        };

        loadP5();

        return () => {
            p5Instance?.remove();
        };
    }, []);

    return <div ref={sketchRef} />;
}
