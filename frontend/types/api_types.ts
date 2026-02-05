export interface API_Form{
    id: string;
    spell_school: string;
    latin_title: string;
    sanskrit_title: string;
    gaelic_title: string;
    polynesian_title: string;
    benoue_title: string;
    algonquian_title: string;
    binary_code: string;
}

export interface API_Power {
    id: string;
    tier: number;
    binary_code: string;
}

export interface API_Shape {
    id: string;
    delivery_name: string;
    delivery_type: string;
    binary_code:string;
}

export interface API_Target {
    id:string;
    name: string;
    binary_code: string;
    binary_code_connected: string;
}

export interface API_SubTechnique {
    id: string;
    name: string;
    binary_code: string;
}

export interface API_Technique {
    name: string;
    id: string;
    binary_code: string;
    sub_techniques: API_SubTechnique[];
}