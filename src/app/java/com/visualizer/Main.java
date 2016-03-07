/**
 * Main.java
 *
 * This file is subject to the terms and conditions defined in
 * file 'LICENSE', which is part of this source code package.
 *
 * Copyright (C) 2016, Matthew Fong
 */
package com.visualizer;

import javax.swing.SwingUtilities;

import com.visualizer.ui.Visualizer;

public class Main {

	public static void main(String[] args) {
		// Schedule a job for the event-dispatching thread:
		// creating and showing this application's GUI.
		SwingUtilities.invokeLater(new Runnable() {
			@Override
			public void run() {
				Visualizer visualizer = new Visualizer(args);
				visualizer.createAndShowGUI();
			}
		});
	}
}
