// Package twoFer helps you share with others.
package twofer

// ShareWith lets you share one with "you" or name, and me.
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return "One for " + name + ", one for me."
}
