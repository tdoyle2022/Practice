import { describe, it, expect } from "vitest";
import TestRenderer from 'react-test-renderer';
import {HomePage} from "../components/HomePage.jsx";
import { MemoryRouter } from "react-router-dom";
import { taskConent } from "../App";

describe("HomePage.jsx", () => (
    it("checks if 5 is 5", () => {
        const num = 5
        expect(num).toBe(5)
    })
))