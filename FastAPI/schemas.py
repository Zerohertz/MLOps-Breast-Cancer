from pydantic import BaseModel

class PredictIn(BaseModel):
    feature_a: float
    feature_b: float
    feature_c: float
    feature_d: float
    feature_e: float
    feature_f: float
    feature_g: float
    feature_h: float
    feature_i: float
    feature_j: float
    feature_k: float
    feature_l: float
    feature_m: float
    feature_n: float
    feature_o: float
    feature_p: float
    feature_q: float
    feature_r: float
    feature_s: float
    feature_t: float
    feature_u: float
    feature_v: float
    feature_w: float
    feature_x: float
    feature_y: float
    feature_z: float
    feature_aa: float
    feature_bb: float
    feature_cc: float
    feature_dd: float

class PredictOut(BaseModel):
    target: int