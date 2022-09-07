const CAR_PRODUCTION_BASE_RATE: f64 = 221.0;
const MINS_IN_HOUR: u32 = 60;

fn success_rate(speed: u8) -> f64 {
    match speed {
        0 => 0.0,
        1..=4 => 1.0,
        5..=8 => 0.9,
        9..=10 => 0.77,
        11..=u8::MAX => todo!(),
    }
}

pub fn production_rate_per_hour(speed: u8) -> f64 {
    success_rate(speed) * CAR_PRODUCTION_BASE_RATE * speed as f64
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    production_rate_per_hour(speed) as u32 / MINS_IN_HOUR
}
