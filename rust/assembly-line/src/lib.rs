pub fn production_rate_per_hour(speed: u8) -> f64 {
    return match speed {
        0 => 0.0,
        1 | 2 | 3 | 4 => speed as f64 * 221.0,
        5 | 6 | 7 | 8 => 0.9 * speed as f64 * 221.0,
        9 | 10 => 0.77 * speed as f64 * 221.0,
        11..=u8::MAX => todo!(),
    };
}

pub fn working_items_per_minute(speed: u8) -> u32 {
    return (production_rate_per_hour(speed) / 60.0) as u32;
}
